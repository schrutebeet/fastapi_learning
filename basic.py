# Python class that provides all the functionality for the API.
from fastapi import FastAPI

# create an instance of the class FastAPI and name it app.
app = FastAPI()

# create a GET path/route
@app.get("/")
def root():
  return {"message": "Hello World"}

# Run the program using:
# uvicorn main:app --reload
#  the --reload flag makes the server restart after code changes
# so it is like when the debugger is on.

# FastAPI offers a nice UI to debug requests/responses:
# http://localhost:8000/docs  --for testing endpoints and routes
# http://localhost:8000/redoc --same