from fastapi import FastAPI
from database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

from routers.DetectRoute import Detectroute
from routers.userRoute import UserRouter
from routers.humanizeRoute import HumanizeRouter

app = FastAPI(title="Huminize API",  version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def main():
    return {"response":"HI There! "}

app.include_router(UserRouter)
app.include_router(HumanizeRouter)
app.include_router(Detectroute)