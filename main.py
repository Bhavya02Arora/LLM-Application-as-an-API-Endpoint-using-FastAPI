from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
	return {"item_id": item_id, "q": q}

# http://127.0.0.1:8000/items/29?q=covidpoly
