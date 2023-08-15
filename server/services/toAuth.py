from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from server.db.database import get_db
from server.db.session import get_pwd_context
from server.schemas.token import TokenData
from server.models.user import User


SECRET_KEY = "983885f48547befc2f27fb040d508e1aa5accab6f7b261fca54c6341a7ca54f7"
ALGORITHM = "HS256"

pwd_context = get_pwd_context()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False

    return user


def verify_password(password, db_password):
    return pwd_context.verify(password, db_password)


def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception

        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception

    user = get_user(db, username=token_data.username)
    if user is None:
        raise credential_exception
    return user
