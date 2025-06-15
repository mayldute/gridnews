import uuid
from datetime import datetime
from typing import List

from sqlalchemy import String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.models.enums import EventStatusEnum


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    series_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('series.id', ondelete='CASCADE'), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[EventStatusEnum] = mapped_column(
        Enum(EventStatusEnum), default=EventStatusEnum.upcoming, nullable=False
    )

    series: Mapped['RacingSeries'] = relationship('RacingSeries', back_populates='events')
    grids: Mapped[List['StartingGrid']] = relationship('StartingGrid', back_populates='event')
