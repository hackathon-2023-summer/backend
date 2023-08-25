# レシピ食材の一覧
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from server.db.database import get_db
from server.schemas.token import TokenData
from server.services.toRecipesequence import create
from server.services.toAuth import get_current_user
from server.schemas.recipeSequence import RecipeSequence, RecipeSequenceCreate
from server.models.recipeSequence import RecipeSequence as RecipeSequenceModel

router = APIRouter()

# リクエストボディからレシピ順を作成して、データベースに保存する
@router.post("/sequences/", response_model=RecipeSequence)
async def create_sequence(
    sequence: RecipeSequenceCreate,
    current_user: TokenData = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create(db=db, recipe_id=sequence.recipe_id, sequence=sequence)

@router.get("/sequences/")
def get_sequences_for_recipe(
    recipe_id: int,
    db: Session = Depends(get_db),
    current_user: TokenData = Depends(get_current_user),
) -> List[RecipeSequence]:
    # データベースから指定レシピの手順を取得
    recipeSequences = (
        db.query(RecipeSequenceModel)
        .filter(
            RecipeSequenceModel.recipe_id == recipe_id,
        )
        .all()
    )
    return recipeSequences

# @router.post("/recipes/{recipe_id}/sequences/", response_model=RecipeSequence)
# async def create_recipesequence(
#     recipe_id: int,
#     sequence: RecipeSequenceCreate,
#     current_user: TokenData = Depends(get_current_user),
#     db: Session = Depends(get_db),
# ):
#     # レシピIDに対応するレシピを取得
#     recipe = db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()

#     # レシピが存在しない、または現在のユーザーがレシピの所有者でない場合はエラー
#     if recipe is None or recipe.user_id != current_user.id:
#         raise HTTPException(
#             status_code=403, detail="Not authorized to add ingredients to this recipe"
#         )

#     return create(db=db, recipe_id=recipe_id, sequence=sequence)
