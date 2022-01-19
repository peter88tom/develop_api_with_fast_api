from jose import JWTError, jwt
from datetime import datetime, timedelta

"""
Three things we need to provide
1/ Secret_key
2/ Algorithm
3/ Exparation time
"""

SECRET_KEY = "c39bb456133e99776f91e70886a605470451af0957d461bf801f86eea518da16"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
  to_encode = data.copy()

  expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

  return encoded_jwt
