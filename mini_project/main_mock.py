from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# To create tables
class Item(BaseModel):
    id: int
    name: str
    description: str
    price: str
    on_offer: bool

@app.get("/")
def home():
    return {"message": "Hello world"}

@app.get("/greet_simple/{name}") # Must specify as a parameter
def greet(name: str):
    return f"Hi, {name.capitalize()}."

# Update an item
@app.put("/item/{item_id}")
def update_item(item_id: int, item:Item):
    return {
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "on_offer": item.on_offer
            }

@app.get("/greet") # Optional as query (name=XXX)
def greet_optional_name(name: Optional[str]="Ricky"):
    return {"message": f"Hello, {name}"}