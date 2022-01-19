from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas, database, utils

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(user_credentials: schemas.UserLogin , db: Session = Depends(database.get_db)):

  user = db.query(models.User).filter(models.User.email == user_credentials.email).first()

  # Check if user does not exist in the db
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials provided")

  # Verify user password
  if not utils.verifty(user_credentials.password, user.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials provided")

  # Create token
  # return token
  return {"token": "example Token"}


