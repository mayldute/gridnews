from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class StartingGridCreate(BaseModel):
    event_id: UUID = Field(
        ...,
        description='Event ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    driver_id: UUID = Field(
        ...,
        description='Driver ID',
        example='443e4321-e89b-12d3-a456-426614174000'
    )
    position: int = Field(
        ...,
        description='Driver position on the grid',
        example=2
    ) 


class StartingGridResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Event ID',
        example='087e1234-e89b-12d3-a456-426614174000'
    )
    event_id: UUID = Field(
        ...,
        description='Event ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    driver_id: UUID = Field(
        ...,
        description='Driver ID',
        example='443e4321-e89b-12d3-a456-426614174000'
    )
    position: int = Field(
        ...,
        description='Driver position on the grid',
        example=2
    ) 
    created_at: datetime = Field(
        ...,
        description='Grid creation time',
        example='2023-10-01T10:00:00Z'
    )
    updated_at: datetime = Field(
        ...,
        description='Grid updated time',
        example='2023-10-01T10:00:00Z'
    )

    model_config = ConfigDict(from_attributes=True)


class StartingGridUpdate(BaseModel):
    event_id: UUID | None = Field(
        None,
        description='Event ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    driver_id: UUID | None = Field(
        None,
        description='Driver ID',
        example='443e4321-e89b-12d3-a456-426614174000'
    )
    position: int | None = Field(
        None,
        description='Driver position on the grid',
        example=2
    ) 