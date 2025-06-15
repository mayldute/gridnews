import uuid
from datetime import datetime, timezone
from typing import List, Optional

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Boolean, DateTime, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base import Base
from app.models.enums import UserRoleEnum


class User(Base):
    __tablename__ = 'users'

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    avatar_url: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    role: Mapped[UserRoleEnum] = mapped_column(
        Enum(UserRoleEnum), default=UserRoleEnum.user, nullable=False
    )

    comments: Mapped[List['Comment']] = relationship('Comment', back_populates='user')
    likes: Mapped[List['Like']] = relationship('Like', back_populates='user')
    subscriptions: Mapped[List['Subscription']] = relationship('Subscription', back_populates='user')
    notification: Mapped[Optional['NotificationSetting']] = relationship(
        'NotificationSetting', back_populates='user', uselist=False
    )
