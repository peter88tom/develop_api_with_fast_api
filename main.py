from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

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
def create_posts(payload: dict = Body(...)):
  print(payload)
  return {"message": f"title {payload['title']} content: {payload['content']}"}
