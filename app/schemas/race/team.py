from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class TeamCreate(BaseModel):
    series_id: UUID = Field(
        ...,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    name: str = Field(
        ...,
        description='Team name',
        example='Macclaren'
    )
    points: int = Field(
        ...,
        description='Team points',
        example=28,
    )
    position: int = Field(
        ...,
        description='Team position in championship',
        example=3
    )


class TeamResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Team ID',
        example='443e4321-e89b-12d3-a456-426614174000'
    )
    series_id: UUID = Field(
        ...,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    name: str = Field(
        ...,
        description='Team name',
        example='Macclaren'
    )
    points: int = Field(
        ...,
        description='Team points',
        example=28,
    )
    position: int = Field(
        ...,
        description='Team position in championship',
        example=3
    )

    model_config = ConfigDict(from_attributes=True)


class TeamUpdate(BaseModel):
    series_id: UUID | None = Field(
        None,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    name: str | None = Field(
        None,
        description='Team name',
        example='Macclaren'
    )
    points: int | None = Field(
        None,
        description='Team points',
        example=28,
    )
    position: int | None = Field(
        None,
        description='Team position in championship',
        example=3
    )
