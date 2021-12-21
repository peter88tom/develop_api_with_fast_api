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


# Delete a post
def find_index_post(id):
  for i, p in enumerate(my_posts):
    if p["id"] == id:
      return i

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



# Delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
  # delete a post
  # find the index in the array for request id and pop it out of array
  index = find_index_post(id)
  if index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} does not exists")
  my_posts.pop(index)
  return Response(status_code=status.HTTP_204_NO_CONTENT)



# Update a post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
  index = find_index_post(id)
  if index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} does not exists")
  post_dict = post.dict()
  post_dict["id"] = id
  print(post_dict)
  my_posts[index] = post_dict
  return {"data": post_dict}




