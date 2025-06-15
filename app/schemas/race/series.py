from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict


class RacingSeriesCreate(BaseModel):
    name: str = Field(
        ...,
        description='Series name',
        example='Formula 1'
    )
    description: str = Field(
        ...,
        description='Series description',
        example=('Formula 1 is a complex sport. The technical and sporting '
        'regulations extend to over 200 pages and there is a supplementary '
        'financial set of rules for the teams and a sporting code for drivers.')
    )
    logo_url: str = Field(
        ...,
        description='Series logo',
        example='https://cdn.example.com/logo/photo.jpg'
    )


class RacingSeriesResponse(BaseModel):
    id: UUID = Field(
        ...,
        description='Series ID',
        example='123e1234-e89b-12d3-a456-426614174000'
    )
    name: str = Field(
        ...,
        description='Series name',
        example='Formula 1'
    )
    description: str = Field(
        ...,
        description='Series description',
        example=('Formula 1 is a complex sport. The technical and sporting '
        'regulations extend to over 200 pages and there is a supplementary '
        'financial set of rules for the teams and a sporting code for drivers.')
    )
    logo_url: str = Field(
        ...,
        description='Series logo',
        example='https://cdn.example.com/logo/photo.jpg'
    )

    model_config = ConfigDict(from_attributes=True)


class RacingSeriesUpdate(BaseModel):
    name: str | None = Field(
        None,
        description='Series name',
        example='Formula 1'
    )
    description: str | None = Field(
        None,
        description='Series description',
        example=('Formula 1 is a complex sport. The technical and sporting '
        'regulations extend to over 200 pages and there is a supplementary '
        'financial set of rules for the teams and a sporting code for drivers.')
    )
    logo_url: str | None = Field(
        None,
        description='Series logo',
        example='https://cdn.example.com/logo/photo.jpg'
    )
