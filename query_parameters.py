"""
Query parameters are optional parameters, which 
are some key-value pairs that appear after the question 
mark(?) in the URL. Note that the question mark sign is 
used to separate path and query parameters.
"""

from fastapi import FastAPI

app = FastAPI()

# dictionary values containing the course names
course_items = [{"course_name": "Python"}, 
                {"course_name": "NodeJS"}, 
                {"course_name": "Machine Learning"}]

@app.get("/courses/")
def read_courses(start: int, end: int):
    # Trims the dictionary to whatever two positions are given
    return course_items[start : start + end]

# The query is the set of key-value pairs that go after 
# the ? in a URL, separated by the & character.
# E.g., http://localhost:8000/courses/?start=0&end=2
# the query is "start=0&end=10".

