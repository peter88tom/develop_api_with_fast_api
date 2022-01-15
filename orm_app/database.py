from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create a database URL for SQLALchemy
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:interface!!@localhost/social_media'

# Create the SQLALchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create database session
SessionLocal = sessionmaker(autocommit=False, autflush=False, bind=engine)

# Create a Base class
Base = declarative_base()
