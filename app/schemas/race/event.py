from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict

from app.models import EventStatusEnum


class EventCreate(BaseModel):
    series_id: UUID = Field(
        ...,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    name: str = Field(
        ...,
        description='Event name',
        example='Monaco GP',
    )
    date: datetime = Field(
        ...,
        description='Event date',
        example='2023-12-01T10:00:00Z'
    )
    location: str = Field(
        ...,
        description='Event location',
        example='Monaco'
    )


class EventResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Event ID',
        example='456e4567-e89b-12d3-a456-426614174000'
    )
    series_id: UUID = Field(
        ...,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    name: str = Field(
        ...,
        description='Event name',
        example='Monaco GP',
    )
    date: datetime = Field(
        ...,
        description='Event date',
        example='2023-12-01T10:00:00Z'
    )
    location: str = Field(
        ...,
        description='Event location',
        example='Monaco'
    )
    status: EventStatusEnum = Field(
        ...,
        description='Event status',
        example='upcoming'
    )

    model_config = ConfigDict(from_attributes=True)


class EventUpdate(BaseModel):
    series_id: UUID | None = Field(
        None,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    name: str | None = Field(
        None,
        description='Event name',
        example='Monaco GP',
    )
    date: datetime | None = Field(
        None,
        description='Event date',
        example='2023-12-01T10:00:00Z'
    )
    location: str | None = Field(
        None,
        description='Event location',
        example='Monaco'
    )
