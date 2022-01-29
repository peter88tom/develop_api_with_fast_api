from pydantic import  BaseModel, EmailStr
from datetime import  datetime
from typing import Optional

# Define base model
class PostBase(BaseModel):
  title: str
  content: str
  published: bool = True


# Extend base model
class CreatePost(PostBase):
  pass



# Define what to return after user created
class CreateUserResponse(BaseModel):
  id: int
  email : EmailStr
  created_at: datetime

  class Config:
    orm_mode= True

# Define what field to return on response
class Post(PostBase):
  id: int
  created_at: datetime
  owner_id: int
  owner: CreateUserResponse

  """
  Add class Config to tell pydantic model to read the data
  even if it is not dictionary but an orm model or any other
  arbitrary object with attributes
  """
  class Config:
    orm_mode= True


# Create user
class CreateUser(BaseModel):
  email :EmailStr
  password: str


# Expected data when user try to login
class UserLogin(BaseModel):
  email: EmailStr
  password: str


# Schema for provided token
class Token(BaseModel):
  access_token: str
  token_type: str

# Schema for data embedded in the token
class TokenData(BaseModel):
  id: Optional[str] = None
