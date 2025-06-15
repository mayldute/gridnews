from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class NotificationSettingsResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Notification settings ID',
        example='136e9572-e89b-12d3-a456-426614174000'
    )
    user_id: UUID = Field(
        ...,
        description='User ID',
        example='123e4567-e89b-12d3-a456-426614174000'
    )
    email_notifications: bool = Field(
        ...,
        description='Email notification setting',
        example=True
    )
    news_notifications: bool = Field(
        ...,
        description='News notification setting',
        example=True
    )
    event_notifications: bool = Field(
        ...,
        description='Event notification setting',
        example=True
    )
    grid_notifications: bool = Field(
        ...,
        description='Grid notification setting',
        example=True
    )

    model_config = ConfigDict(from_attributes=True)


class NotificationSettingsUpdate(BaseModel):
    email_notifications: bool | None = Field(
        None,
        description='Email notification setting',
        example=True
    )
    news_notifications: bool | None = Field(
        None,
        description='News notification setting',
        example=True
    )
    event_notifications: bool | None = Field(
        None,
        description='Event notification setting',
        example=True
    )
    grid_notifications: bool | None = Field(
        None,
        description='Grid notification setting',
        example=True
    )