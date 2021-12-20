from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
  title: str
  content: str

"""
Test function to check if the environment installed works collect

To run the app we use "uvicorn main: app --reload" command

Descriptions
---------------
uvicorn is a server
main is the name of the file
app is the instance of fastapi
--reload tells uvicorn to automatically reload the code every time we make changes
"""


@app.get("/")
async def root():
  return {"message": "Welcome to my social media api"}



@app.get("/posts")
def get_posts():
  """ Test endpoint to return all yours posts """
  return {"data": "This is your posts"}


@app.post("/create_posts")
def create_posts(new_post:Post):
  print(new_post)
  return {"data": new_post}
