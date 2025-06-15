from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from app.models import NewsTypeEnum


class NewsCreate(BaseModel):
    series_id: UUID = Field(
        ...,
        description='Series ID',
        example='123e4567-e89b-12d3-a456-426614174000'
    )
    published_by_id: UUID = Field(
        ...,
        description='Series ID',
        example='456e4567-e89b-12d3-a456-426614174000'
    )
    title: str = Field(
        ...,
        description='News title',
        example='Tsunoda left unhappy with 10-place grid penalty in Canada'
    )
    content: str = Field(
        ...,
        description='News content',
        example=('Tsunoda came across the damaged McLaren on the back straight '
        'and passed Piastri, but was summoned to the stewards after the session for his actions.')
    )
    author: str = Field(
        ...,
        description='News author',
        example='Dmitry Bukharov'
    )
    source: str = Field(
        ...,
        description='News source',
        example='BBC News'
    )
    type: NewsTypeEnum = Field(
        ...,
        description='News type',
        example='news'
    )


class NewsResponse(BaseModel):
    series_id: UUID = Field(
        ...,
        description='Series ID',
        example='123e4567-e89b-12d3-a456-426614174000'
    )
    published_by_id: UUID = Field(
        ...,
        description='Series ID',
        example='456e4567-e89b-12d3-a456-426614174000'
    )
    title: str = Field(
        ...,
        description='News title',
        example='Tsunoda left unhappy with 10-place grid penalty in Canada'
    )
    content: str = Field(
        ...,
        description='News content',
        example=('Tsunoda came across the damaged McLaren on the back straight '
        'and passed Piastri, but was summoned to the stewards after the session for his actions.')
    )
    author: str = Field(
        ...,
        description='News author',
        example='Dmitry Bukharov'
    )
    source: str = Field(
        ...,
        description='News source',
        example='BBC News'
    )
    type: NewsTypeEnum = Field(
        ...,
        description='News type',
        example='news'
    )
    created_at: datetime = Field(
        ...,
        description='News creation time',
        example='2023-10-01T10:00:00Z'
    )
    updated_at: datetime = Field(
        ...,
        description='News creation time',
        example='2023-11-01T10:00:00Z'
    )
    views_count: int = Field(
        ...,
        description='Views count',
        example=1000
    )

    model_config = ConfigDict(from_attributes=True)


class NewsUpdate(BaseModel):
    series_id: UUID | None = Field(
        None,
        description='Series ID',
        example='123e4567-e89b-12d3-a456-426614174000'
    )
    published_by_id: UUID | None = Field(
        None,
        description='Published by ID',
        example='456e4567-e89b-12d3-a456-426614174000'
    )
    title: str | None = Field(
        None,
        description='News title',
        example='Tsunoda left unhappy with 10-place grid penalty in Canada'
    )
    content: str | None = Field(
        None,
        description='News content',
        example=('Tsunoda came across the damaged McLaren on the back straight '
                 'and passed Piastri, but was summoned to the stewards after the session for his actions.')
    )
    author: str | None = Field(
        None,
        description='News author',
        example='Dmitry Bukharov'
    )
    source: str | None = Field(
        None,
        description='News source',
        example='BBC News'
    )
    type: NewsTypeEnum | None = Field(
        None,
        description='News type',
        example='news'
    )
