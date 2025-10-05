from __future__ import annotations
import uuid
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, conint, ConfigDict
from enum import Enum

UserId = uuid.UUID
ThreadId = uuid.UUID
CommentId = uuid.UUID
ItemId = uuid.UUID

# --- Enums for controlled vocabularies ---
class ThreadType(str, Enum):
    ITEM_DISCUSSION = "item_discussion"
    GENERAL_CHAT = "general_chat"

class VoteDirection(int, Enum):
    DOWNVOTE = -1
    NEUTRAL = 0
    UPVOTE = 1

# --- Vote Models ---
class VoteBase(BaseModel):
    user_id: UserId = Field(description="The unique identifier of the user who is voting.")
    direction: VoteDirection = Field(description="The direction of the vote: 1 for upvote, -1 for downvote.")

class VoteCreate(VoteBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "user_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "direction": 1
            }
        }
    )

# --- Comment Models ---
class CommentBase(BaseModel):
    author_id: UserId = Field(description="The unique identifier of the user who wrote the comment.")
    content: str = Field(min_length=1, description="The content of the comment.")
    parent_comment_id: Optional[CommentId] = Field(None, description="The ID of the comment this is a reply to. Null for top-level comments.")

class CommentCreate(CommentBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "author_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "content": "This is a very helpful comment!",
                "parent_comment_id": None
            }
        }
    )

class CommentUpdate(BaseModel):
    content: str = Field(min_length=1, description="The new content of the comment.")

class CommentRead(CommentBase):
    comment_id: CommentId = Field(description="The unique identifier for this comment.")
    created_at: datetime = Field(description="The timestamp when the comment was created (UTC).")
    model_config = ConfigDict(from_attributes=True)

# --- Thread Models ---
class ThreadBase(BaseModel):
    author_id: UserId = Field(description="The unique identifier of the user who created the thread.")
    thread_type: ThreadType = Field(description="The type of the thread, e.g., for an item or general chat.")
    item_id: Optional[ItemId] = Field(None, description="The unique identifier of the item this thread is about, if applicable.")
    title: str = Field(min_length=3, max_length=100, description="The title of the discussion thread.")
    content: str = Field(min_length=10, description="The main content or description of the thread.")
    is_active: bool = Field(True, description="Indicates if the thread is active and open for discussion.")

class ThreadCreate(ThreadBase):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "author_id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
                "thread_type": "item_discussion",
                "item_id": "i1i2i3i4-i5i6-i7i8-i9i0-i1i2i3i4i5i6",
                "title": "Discussion about the IKEA Sofa",
                "content": "I saw this sofa listed and had a few questions about its condition.",
                "is_active": True
            }
        }
    )

class ThreadUpdate(BaseModel):
    title: Optional[str] = Field(None, description="The new title of the thread.")
    content: Optional[str] = Field(None, description="The new content of the thread.")
    is_active: Optional[bool] = Field(None, description="The new active status of the thread.")

class ThreadRead(ThreadBase):
    thread_id: ThreadId = Field(description="The unique identifier for this thread.")
    created_at: datetime = Field(description="Timestamp of creation (UTC).")
    updated_at: datetime = Field(description="Timestamp of last update (UTC).")
    comment_count: int = Field(0, description="The total number of comments on this thread.")
    vote_score: int = Field(0, description="The total score (upvotes - downvotes) of this thread.")
    model_config = ConfigDict(from_attributes=True)