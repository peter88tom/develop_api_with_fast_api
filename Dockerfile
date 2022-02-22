FROM python:3.10

# Set a working directory
WORKDIR /usr/src/app

# Copy the requirements to the working directory
COPY requirements.txt ./

# run a command to install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy our source code to current working directory
COPY . .

# give a command when you want to run the container
CMD ["uvicorn", "orm_app_with_routers_using_alembic.main:app", "--host", "0.0.0.0", "--port", "8000"]
