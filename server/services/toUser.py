from sqlalchemy.orm import Session
from server.schemas.user import User
from server.models.user import User as UserModel


def create(db: Session, user: User):
    db_user = UserModel(
        username=user.username, password=user.password, email=user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
