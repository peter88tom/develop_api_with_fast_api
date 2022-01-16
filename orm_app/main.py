from fastapi import Depends, FastAPI, Response, status, HTTPException
from fastapi.params import Body
from typing import  Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

# Create instance
app = FastAPI()

# Database connect
# while True:
#         try:
#           conn = psycopg2.connect(host="localhost", database="social_media", user="postgres",
#                                   password="interface!!", cursor_factory=RealDictCursor)
#           cursor = conn.cursor()
#           print("Database connection was successfully")
#           break
#         except Exception as e:
#           print(e)
#           print("Could not connect to the database")
#           time.sleep(2)

@app.get("/")
def root():
  return {"message": "Hello world"}



# Get list of posts
@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
  # cursor.execute("""SELECT * FROM posts""")
  # posts= cursor.fetchall()
  posts = db.query(models.Post).all()
  return {"data": posts}


# Create a post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.CreatePost, db: Session = Depends(get_db)):
  # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s, %s, %s) RETURNING * """,(
  #                post.title, post.content, post.published),)
  #
  # # Commit changes to the database
  # conn.commit()
  #
  # # Fetch the current created post
  # new_post = cursor.fetchone()

  # Orm create post
  # new_post = models.Post(title=post.title, content=post.content, published=post.published)
  """ If we have too many fields we need to automatically unpack the fields using **post.dict()"""
  new_post = models.Post(**post.dict())
  db.add(new_post)
  db.commit()

  db.refresh(new_post)

  return {"data": new_post}

# Get single post
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
  # cursor.execute(""" SELECT * FROM posts WHERE id=%s """,(str(id)))
  # post = cursor.fetchone()
  post = db.query(models.Post).filter(models.Post.id==id).first()

  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id: {id} was not found")

  return {"data": post}



# Delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
  # delete a post
  # cursor.execute(""" DELETE FROM posts WHERE id=%s RETURNING *""",(str(id),))
  # deleted_post = cursor.fetchone()
  # conn.commit()
  post = db.query(models.Post).filter(models.Post.id == id)

  if post.first() == None:
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"The post with id: {id} does not exists")
  post.delete(synchronize_session=False)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)



# Update a post
@app.put("/posts/{id}")
def update_post(id: int, post: schemas.CreatePost, db: Session = Depends(get_db)):
  # cursor.execute(""" UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *""", (
  #   post.title,
  #   post.content, post.published,str(id)),)
  #
  # updated_post = cursor.fetchone()
  # conn.commit()
  updated_post = db.query(models.Post).filter(models.Post.id == id)

  # Raise an exception if does not exist
  if updated_post.first() == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id: {id} does not exists")

  updated_post.update(post.dict(), synchronize_session=False)
  db.commit()

  return {"data": updated_post.first()}
