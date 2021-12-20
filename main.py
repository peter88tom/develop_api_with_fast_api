from fastapi import FastAPI, Response, status, HTTPException
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

# Method to retrieve a single post
def find_post(id):
  for post in my_posts:
    if post['id'] == id:
      return post



@app.get("/")
def root():
  return {"message": "Hello world"}


# Get list of posts
@app.get("/posts")
def get_posts():
  return {"data": my_posts}


# Create a post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
  post_dict = post.dict()

  # Generate random id
  post_dict['id'] = randrange(0,1000000)

  # Append the new post
  my_posts.append(post_dict)
  return {"data": post}

# Get single post
@app.get("/posts/{id}")
def get_post(id: int):
  post = find_post(id)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id: {id} was not found")
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {"message": f"post with {id} was not found"}
  return {"data": post}



