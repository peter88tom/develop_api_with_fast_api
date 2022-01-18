from passlib.context import CryptContext


# Tell passlib what is the default hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Hash the password
def hash_password(password):
  return pwd_context.hash(password)

