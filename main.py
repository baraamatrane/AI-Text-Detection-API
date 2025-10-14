from fastapi import FastAPI

app = FastAPI(title="Huminize API",  version="1.0.0")

products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Tablet", "price": 299.99},
]

@app.get("/")
async def main():
    return {"response":"HI There! "}

@app.get("/products")
async def Products(name: str = None):
    if name:
        return [product for product in products if product["name"] == name]
    return products