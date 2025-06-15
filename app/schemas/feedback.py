from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class CommentCreate(BaseModel):
    news_id: UUID = Field(
        ...,
        description='News ID',
        example='789e4567-e89b-12d3-a456-426614174000'
    )
    user_id: UUID = Field(
        ...,
        description='User ID',
        example='012e4567-e89b-12d3-a456-426614174000'
    )
    content: str = Field(
        ...,
        description='Comment content',
        example='Tsunods is right.'
    )


class CommentResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Comment ID',
        example='111e4567-e89b-12d3-a456-426614174000'
    )
    news_id: UUID = Field(
        ...,
        description='News ID',
        example='789e4567-e89b-12d3-a456-426614174000'
    )
    user_id: UUID = Field(
        ...,
        description='User ID',
        example='012e4567-e89b-12d3-a456-426614174000'
    )
    content: str = Field(
        ...,
        description='Comment content',
        example='Tsunods is right.'
    )
    created_at: datetime = Field(
        ...,
        description='Comment creation time',
        example='2023-10-01T10:00:00Z'
    )

    model_config = ConfigDict(from_attributes=True)


class CommentApproval(BaseModel):
    is_approved: bool = Field(
        ...,
        description="Is comment approved",
        example=True
    )