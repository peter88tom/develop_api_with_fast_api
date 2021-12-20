from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import  Optional
from random import randrange

# Create instance
app = FastAPI()

# Define fields
class Post(BaseModel):
  title: str
  content: str
  published: bool  = True
  rating: Optional[int] = None

# Define default data
my_posts = [
  {"id":1, "title": "Post 1", "content": "Content of post 1"},
  {"id":2, "title": "Post 2", "content": "Content of post 2"},
  {"id":3, "title": "Post 3", "content": "Content of post 3"},
]

@app.get("/")
def root():
  return {"message": "Hello world"}


# Get list of posts
@app.get("/posts")
def get_posts():
  return {"data": my_posts}


# Create a post
@app.post("/posts")
def create_post(post: Post):
  post_dict = post.dict()

  # Generate random id
  post_dict['id'] = randrange(0,1000000)

  # Append the new post
  my_posts.append(post_dict)
  return {"data": post}


