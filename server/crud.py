import schemas, models
from sqlalchemy.orm import Session

#ユーザー登録
def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username, password=user.password, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user