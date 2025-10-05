from __future__ import annotations

import os

from fastapi import FastAPI, HTTPException, Query, status
from uuid import UUID, uuid4
from typing import List, Optional

from models.item import*
from models.thread import*

port = int(os.environ.get("FASTAPIPORT", 8000))

app = FastAPI(
    title="Item & Thread API",
    description="Item and Thread microservice",
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

# =============================================================================
#  THREAD MODEL (3 parts)
# =============================================================================
# =============================================================================
#  THREADS
# =============================================================================
@app.post("/threads", response_model=ThreadRead, status_code=status.HTTP_201_CREATED, tags=["Threads"])
def create_thread(thread: ThreadCreate):
    # In a real app, you would implement the database logic here.
    # For now, it's a placeholder.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@app.get("/threads", response_model=List[ThreadRead], tags=["Threads"])
def list_threads():
    # Logic to list all threads from the database.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@app.get("/threads/{thread_id}", response_model=ThreadRead, tags=["Threads"])
def get_thread(thread_id: ThreadId):
    # Logic to get a single thread by its ID.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@app.patch("/threads/{thread_id}", response_model=ThreadRead, tags=["Threads"])
def update_thread(thread_id: ThreadId, update_data: ThreadUpdate):
    # Logic to update a thread's details.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@app.delete("/threads/{thread_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Threads"])
def delete_thread(thread_id: ThreadId):
    # Logic to delete a thread.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

# =============================================================================
#  COMMENTS
# =============================================================================
@app.post("/threads/{thread_id}/comments", response_model=CommentRead, status_code=status.HTTP_201_CREATED, tags=["Comments"])
def create_comment(thread_id: ThreadId, comment: CommentCreate):
    # Logic to create a comment for the given thread_id.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@app.get("/threads/{thread_id}/comments", response_model=List[CommentRead], tags=["Comments"])
def list_comments_for_thread(thread_id: ThreadId):
    # Logic to list all comments for the given thread_id.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@app.patch("/threads/{thread_id}/comments/{comment_id}", response_model=CommentRead, tags=["Comments"])
def update_comment(thread_id: ThreadId, comment_id: CommentId, update_data: CommentUpdate):
    # Logic to update a specific comment.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@app.delete("/threads/{thread_id}/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Comments"])
def delete_comment(thread_id: ThreadId, comment_id: CommentId):
    # Logic to delete a specific comment.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

# =============================================================================
#  VOTES
# =============================================================================
@app.put("/threads/{thread_id}/vote", response_model=ThreadRead, tags=["Votes"])
def cast_or_update_vote(thread_id: ThreadId, vote: VoteCreate):
    """
    Casts or updates a user's vote on a thread.
    This is an "upsert" operation.
    """
    # Logic to find the thread and update its score based on the user's vote.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

@app.delete("/threads/{thread_id}/vote", response_model=ThreadRead, tags=["Votes"])
def cancel_vote(thread_id: ThreadId, user_identifier: VoteBase):
    """
    Cancels a user's vote on a thread.
    This sets the user's vote to NEUTRAL or removes it entirely.
    """
    # In a real app, you'd get the user_id from an auth token.
    # Here, we expect it in the request body for demonstration.
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)

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
