import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, DateTime, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .video_snapshots import VideoSnapshot


class Video(Base):
    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    creator_id: Mapped[uuid.UUID] = mapped_column(UUID, nullable=False)
    video_created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    views_count: Mapped[int]
    likes_count: Mapped[int]
    comments_count: Mapped[int]
    reports_count: Mapped[int]

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=lambda: datetime.now(timezone.utc),
        default=lambda: datetime.now(timezone.utc),
    )

    snapshots: Mapped[list["VideoSnapshot"]] = relationship(back_populates="video", uselist=True)
