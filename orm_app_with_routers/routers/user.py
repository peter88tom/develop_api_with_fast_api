from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter()


@router.post("/users", status_code=status.HTTP_201_CREATED,response_model=schemas.CreateUserResponse)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
  # Hash the password - user.password
  user.password = utils.hash_password(user.password)

  new_user = models.User(**user.dict())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user



# Get information about user
@router.get("/user/{id}", response_model= schemas.CreateUserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
  user = db.query(models.User).filter(models.User.id == id).first()

  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"User with id: {id} does not exist")
  return  user
