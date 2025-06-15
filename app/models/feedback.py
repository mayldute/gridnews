import uuid
from datetime import datetime, timezone

from sqlalchemy import Text, DateTime, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    news_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('news.id', ondelete='CASCADE'), nullable=False
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    is_approved: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    user: Mapped['User'] = relationship('User', back_populates='comments')
    news: Mapped['News'] = relationship('News', back_populates='comments')


class Like(Base):
    __tablename__ = 'likes'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    news_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('news.id', ondelete='CASCADE'), nullable=False
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    user: Mapped['User'] = relationship('User', back_populates='likes')
    news: Mapped['News'] = relationship('News', back_populates='likes')

    __table_args__ = (
        UniqueConstraint('news_id', 'user_id', name='uq_like_news_user'),
    )
