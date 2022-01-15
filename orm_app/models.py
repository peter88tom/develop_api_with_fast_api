from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
  __tablename__ = 'posts'

  id = Column(Integer, primary_key=True, nullable=False)
  title = Column(String, nullable=False)
  content = Column(String, nullable=False)
  published = Column(Boolean, default=True)
