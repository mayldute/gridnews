import uuid
from typing import List

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class Driver(Base):
    __tablename__ = 'drivers'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    series_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('series.id', ondelete='CASCADE'), nullable=False
    )
    team_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('teams.id', ondelete='CASCADE'), nullable=False
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    number: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    points: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    position: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    series: Mapped['RacingSeries'] = relationship('RacingSeries', back_populates='drivers')
    team: Mapped['Team'] = relationship('Team', back_populates='drivers')
    grids: Mapped[List['StartingGrid']] = relationship('StartingGrid', back_populates='driver')