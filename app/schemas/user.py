from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict

from app.models import UserRoleEnum


class UserCreate(BaseModel):
    email: EmailStr = Field(
        ...,
        description='User email address',
        example='user@example.com'
    )
    username: str = Field(
        ...,
        description='User username',
        example='username'
    )


class UserResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='User ID', 
        example='123e4567-e89b-12d3-a456-426614174000'
    )
    email: EmailStr = Field(
        ...,
        description='User email address',
        example='user@example.com'
    )
    username: str = Field(
        ...,
        description='User username',
        example='username'
    )
    avatar_url: str = Field(
        ..., 
        description='User avatar URL',
        example='https://cdn.example.com/avatar/photo.jpg'
    )
    created_at: datetime = Field(
        ...,
        description='Account creation time',
        example='2023-10-01T10:00:00Z'
    )
    is_active: bool = Field(
        ...,
        description='Is account active',
        example='True'
    )
    role: UserRoleEnum = Field(
        ...,
        description='User role',
        example='User'
    )

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: EmailStr | None = Field(
        None,
        description='Users email address',
        example='user@example.com'
    )
    username: str | None = Field(
        None,
        description='Users username',
        example='username'
    )
    avatar_url: str | None = Field(
        None, 
        description='Users avatar',
        example='https://cdn.example.com/avatar/photo.jpg'
    )