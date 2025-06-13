import uuid
from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy import Integer, String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.models.enums import EventStatusEnum


class RacingSeries(Base):
    __tablename__ = 'series'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    logo_url: Mapped[str] = mapped_column(String, nullable=False)

    news: Mapped[List['News']] = relationship('News', back_populates='series')
    events: Mapped[List['Event']] = relationship('Event', back_populates='series')
    drivers: Mapped[List['Driver']] = relationship('Driver', back_populates='series')
    teams: Mapped[List['Team']] = relationship('Team', back_populates='series')
    subscriptions: Mapped[List['Subscription']] = relationship('Subscription', back_populates='series')


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
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


class Driver(Base):
    __tablename__ = 'drivers'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    series_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('series.id', ondelete='CASCADE'), nullable=False
    )
    team_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('teams.id', ondelete='CASCADE'), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    points: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    position: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    series: Mapped['RacingSeries'] = relationship('RacingSeries', back_populates='drivers')
    team: Mapped['Team'] = relationship('Team', back_populates='drivers')
    grids: Mapped[List['StartingGrid']] = relationship('StartingGrid', back_populates='driver')


class Team(Base):
    __tablename__ = 'teams'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    series_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('series.id', ondelete='CASCADE'), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    points: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    position: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    series: Mapped['RacingSeries'] = relationship('RacingSeries', back_populates='teams')
    drivers: Mapped[List['Driver']] = relationship('Driver', back_populates='team')


class StartingGrid(Base):
    __tablename__ = 'grids'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True)
    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('events.id', ondelete='CASCADE'), nullable=False
    )
    driver_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('drivers.id', ondelete='CASCADE'), nullable=False
    )
    position: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)

    event: Mapped['Event'] = relationship('Event', back_populates='grids')
    driver: Mapped['Driver'] = relationship('Driver', back_populates='grids')
