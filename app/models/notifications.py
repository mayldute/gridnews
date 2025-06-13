import uuid
from datetime import datetime, timezone

from sqlalchemy import ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class Subscription(Base):
    __tablename__ = 'subscriptions'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
    series_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('series.id', ondelete='CASCADE'), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    user: Mapped['User'] = relationship('User', back_populates='subscriptions')
    series: Mapped['RacingSeries'] = relationship('RacingSeries', back_populates='subscriptions')


class NotificationSetting(Base):
    __tablename__ = 'notifications'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=False
    )
    email_notifications: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    news_notifications: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    event_notifications: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    grid_notifications: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    user: Mapped['User'] = relationship('User', back_populates='notification', uselist=False)
