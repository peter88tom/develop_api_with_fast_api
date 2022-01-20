from fastapi import APIRouter, Depends, status, Response, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas, database, utils, oauth2

router = APIRouter(tags=['Authentication'])

# @router.post("/login")
# def login(user_credentials: schemas.UserLogin , db: Session = Depends(database.get_db)):
#
#   user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
#
#   # Check if user does not exist in the db
#   if not user:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials provided")
#
#   # Verify user password
#   if not utils.verifty(user_credentials.password, user.password):
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials provided")
#
#   # Create token
#   access_token = oauth2.create_access_token(data={"user_id": user.id})
#   return {
#     "access_token": access_token,
#     "token_type": "bearer",
#   }


"""
Instead of using the body(schemas.UserLogin) as define as above code, we gonna be using fastapi build library
called OAuth2PasswordRequestForm to retrieve the information send by user

This form uses username and not email,
{
"username": "some_user_name",
"password": "some password"
}
"""
@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):

  user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

  # Check if user does not exist in the db
  if not user:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials provided")

  # Verify user password
  if not utils.verifty(user_credentials.password, user.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid credentials provided")

  # Create token
  access_token = oauth2.create_access_token(data={"user_id": user.id})
  return {
    "access_token": access_token,
    "token_type": "bearer",
  }

