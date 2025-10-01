from __future__ import annotations

import os

from fastapi import FastAPI, HTTPException, Query, status
from uuid import UUID, uuid4
from models.item import *

port = int(os.environ.get("FASTAPIPORT", 8000))

app = FastAPI(
    title="Item API",
    description="Item and Post microservice",
    version="0.1.0",
)


# -----------------------------------------------------------------------------
# Item endpoints
# -----------------------------------------------------------------------------
@app.post("/items", response_model=ItemRead, status_code=201, tags=["Items"])
def create_item(item: ItemBase):
    """
    Create a new item record.
    """
    raise HTTPException(
        status_code=501,
        detail="The 'create_item' functionality is not yet implemented."
    )


@app.get("/items", response_model=List[ItemRead], tags=["Items"])
def list_items(
        item_id: Optional[UUID] = Query(None, description="Filter by item's id"),
        category: Optional[CategoryType] = Query(None, description="Filter by item's category"),
        transaction_type: Optional[TransactionType] = Query(None, description="Filter by item's transaction type")
):
    """Get a list of all items, with optional filtering."""
    raise HTTPException(
        status_code=501,
        detail="The 'list_items' functionality is not yet implemented."
    )


@app.get("/items/{item_id}", response_model=ItemRead, tags=["Items"])
def get_item(item_id: UUID):
    """Get a single item by its id."""
    raise HTTPException(
        status_code=501,
        detail="The 'get_item' functionality is not yet implemented."
    )


@app.patch("/items/{item_id}", response_model=ItemRead, tags=["Items"])
def update_item(item_id: UUID, update_data: ItemUpdate):
    """Partially update an item's information."""
    raise HTTPException(
        status_code=501,
        detail="The 'update_item' functionality is not yet implemented."
    )


@app.delete("/items/{item_id}", status_code=204, tags=["Items"])
def delete_item(item_id: UUID):
    """Delete an item."""
    raise HTTPException(
        status_code=501,
        detail="The 'delete_item' functionality is not yet implemented."
    )


# -----------------------------------------------------------------------------
# Root
# -----------------------------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Welcome to the ItemPost API. See /docs for OpenAPI UI."}


# -----------------------------------------------------------------------------
# Entrypoint for `python main.py`
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)
