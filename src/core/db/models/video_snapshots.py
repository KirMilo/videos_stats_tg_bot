import uuid
from datetime import datetime, timezone
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, DateTime, UUID, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .videos import Video


class VideoSnapshot(Base):
    __tablename__ = "video_snapshots"

    id: Mapped[uuid.UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    video_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("videos.id"))
    views_count: Mapped[int] = mapped_column(Integer, default=0)
    likes_count: Mapped[int] = mapped_column(Integer, default=0)
    comments_count: Mapped[int] = mapped_column(Integer, default=0)
    reports_count: Mapped[int] = mapped_column(Integer, default=0)

    delta_views_count: Mapped[int] = mapped_column(Integer, default=0)
    delta_likes_count: Mapped[int] = mapped_column(Integer, default=0)
    delta_comments_count: Mapped[int] = mapped_column(Integer, default=0)
    delta_reports_count: Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        onupdate=lambda: datetime.now(timezone.utc),
        default=lambda: datetime.now(timezone.utc),
    )

    video: Mapped["Video"] = relationship(back_populates="snapshots")
