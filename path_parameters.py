from fastapi import FastAPI

app = FastAPI()

# define the path parameter
# it can (optionally) be declared with a type so that it casts
# whatever string it is written to that type.
@app.get("/courses/{course_name}")
def read_course(course_name: int):
    return {"course_name": course_name}  #variable will be an int.