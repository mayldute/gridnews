import uuid
from typing import List

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class RacingSeries(Base):
    __tablename__ = 'series'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    logo_url: Mapped[str] = mapped_column(String, nullable=False)

    news: Mapped[List['News']] = relationship('News', back_populates='series')
    events: Mapped[List['Event']] = relationship('Event', back_populates='series')
    drivers: Mapped[List['Driver']] = relationship('Driver', back_populates='series')
    teams: Mapped[List['Team']] = relationship('Team', back_populates='series')
    subscriptions: Mapped[List['Subscription']] = relationship('Subscription', back_populates='series')