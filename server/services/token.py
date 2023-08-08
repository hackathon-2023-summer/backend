from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "983885f48547befc2f27fb040d508e1aa5accab6f7b261fca54c6341a7ca54f7"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt