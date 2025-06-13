import uuid
from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy import Integer, String, Text, Enum, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.models.enums import NewsTypeEnum


class News(Base):
    __tablename__ = 'news'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    series_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('series.id', ondelete='CASCADE'), nullable=False
    )
    published_by_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    source: Mapped[str] = mapped_column(String(255), nullable=False)
    type: Mapped[NewsTypeEnum] = mapped_column(
        Enum(NewsTypeEnum), default=NewsTypeEnum.news, nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    views_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    comments: Mapped[List['Comment']] = relationship('Comment', back_populates='news')
    likes: Mapped[List['Like']] = relationship('Like', back_populates='news')
    series: Mapped['RacingSeries'] = relationship('RacingSeries', back_populates='news')
