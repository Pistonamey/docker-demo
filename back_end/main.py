from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Person(BaseModel):
    id: int
    name: str


DB: List[Person] = [
    Person(id=1, name="Jamila", age=22),
    Person(id=2, name="Alex", age=21)

]


@app.get("/api")
async def root():
    return DB
