from typing import Optional, List
from fastapi import FastAPI, Query

from schemas import Book, User

app = FastAPI()


@app.post("/", response_model=Book)
def read_root(user: User):
    return {'user': user}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
