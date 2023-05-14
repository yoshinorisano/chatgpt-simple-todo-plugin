"""
Simple TODO App for ChatGPT Plugin.
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI()

# A simple in-memory store for the TODO items
todos = {}


class TodoItem(BaseModel):
    title: str
    description: Optional[str] = None


@app.get("/todos", response_model=List[TodoItem])
async def get_todos():
    return list(todos.values())


@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoItem):
    id = max(todos.keys(), default=0) + 1
    todos[id] = todo
    return {"id": id}


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]


@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
async def get_manifest():
    return FileResponse('manifest.json')


# Added manually after code generation.
@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    return FileResponse('openapi.yaml')


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Simple TODO API",
        version="1.0.0",
        description="This is a very simple TODO API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

