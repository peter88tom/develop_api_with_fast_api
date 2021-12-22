from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import  Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# Create instance
app = FastAPI()

# Define fields
class Post(BaseModel):
  title: str
  content: str
  published: bool  = True


# Database connect
while True:
        try:
          conn = psycopg2.connect(host="localhost", database="social_media", user="postgres",
                                  password="interface!!", cursor_factory=RealDictCursor)
          cursor = conn.cursor()
          print("Database connection was successfully")
          break
        except Exception as e:
          print(e)
          print("Could not connect to the database")
          time.sleep(2)

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
  cursor.execute("""SELECT * FROM posts""")
  posts= cursor.fetchall()
  return {"data": posts}


# Create a post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
  cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s, %s, %s) RETURNING * """,(
                 post.title, post.content, post.published))

  # Commit changes to the database
  conn.commit()

  # Fetch the current created post
  new_post = cursor.fetchone()

  return {"data": new_post}

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
  #Find an index of a post by using given id
  index = find_index_post(id)

  # Raise an exception if does not exist
  if index == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} does not exists")

  # If exists convert it into dictionary
  post_dict = post.dict()

  # Set the id to a given id
  post_dict["id"] = id

  # Replace the post index with posted dictionary
  my_posts[index] = post_dict
  return {"data": post_dict}




