from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class DriverCreate(BaseModel):
    series_id: UUID = Field(
        ...,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    team_id: UUID = Field(
        ...,
        description='Team ID',
        example='098e0987-e89b-12d3-a456-426614174000'
    )
    name: str = Field(
        ...,
        description='Driver name',
        example='Lando Noris'
    )
    number: int = Field(
        ...,
        description='Driver number',
        example=4
    )
    points: int = Field(
        ...,
        description='Driver points',
        example=28,
    )
    position: int = Field(
        ...,
        description='Driver position in championship',
        example=3
    )


class DriverResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Driver ID',
        example='443e4321-e89b-12d3-a456-426614174000'
    )
    series_id: UUID = Field(
        ...,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    team_id: UUID = Field(
        ...,
        description='Team ID',
        example='098e0987-e89b-12d3-a456-426614174000'
    )
    name: str = Field(
        ...,
        description='Driver name',
        example='Lando Noris'
    )
    number: int = Field(
        ...,
        description='Driver number',
        example=4
    )
    points: int = Field(
        ...,
        description='Driver points',
        example=28,
    )
    position: int = Field(
        ...,
        description='Driver position in championship',
        example=3
    )

    model_config = ConfigDict(from_attributes=True)


class DriverUpdate(BaseModel):
    series_id: UUID | None = Field(
        None,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    team_id: UUID | None = Field(
        None,
        description='Team ID',
        example='098e0987-e89b-12d3-a456-426614174000'
    )
    name: str | None = Field(
        None,
        description='Driver name',
        example='Lando Noris'
    )
    number: int | None = Field(
        None,
        description='Driver number',
        example=4
    )
    points: int | None = Field(
        None,
        description='Driver points',
        example=28,
    )
    position: int | None = Field(
        None,
        description='Driver position in championship',
        example=3
    )