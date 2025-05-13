from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id : int
    item : str
    price : float
    
##product = Product()
#product.id = 1
#product.item = "Hero"
#product.price = 900.00    