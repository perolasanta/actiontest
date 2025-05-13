from fastapi import FastAPI
from typing import Union
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{itemid}")
def read_items(itemid: int, q: Union [str, None] =  None):
    return {"item_id": itemid, "Q": q }
        
        
    