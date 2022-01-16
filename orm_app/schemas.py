from pydantic import  BaseModel

# Define base model
class PostBase(BaseModel):
  title: str
  content: str
  published: bool = True


# Extend base model
class CreatePost(PostBase):
  pass

