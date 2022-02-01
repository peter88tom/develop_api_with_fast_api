from fastapi import Depends, APIRouter, status, HTTPException, Response, FastAPI
from sqlalchemy.orm import Session
from .. import  schemas, models, database, oauth2



# Setup router
router = APIRouter(
  prefix="/vote",
  tags = ["Vote"]
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db),
         current_user: int = Depends(oauth2.get_current_user)):

  # Check if post exist
  post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()

  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {vote.post_id} does not exist")

  # Check if user has already voted for this post
  query_vote  = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id,
                                            models.Vote.user_id == current_user.id)

  found_vote = query_vote.first()
  if (vote.dir==1):
    # Check if this use
    if found_vote:
      # User has voted for this post
      raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                          detail=f"User with {current_user.id } have already voted for post with id: {vote.post_id}")
    new_vote = models.Vote(user_id = current_user.id, post_id = vote.post_id)
    db.add(new_vote)
    db.commit()

    return {"message": "Successfully added vote"}
  else:
    if not found_vote:
      raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, deatils="Vote does not exist")
    query_vote.delete(synchronize_session=False)
    db.commit()
    return {"message": "Vote deleted successfully"}
