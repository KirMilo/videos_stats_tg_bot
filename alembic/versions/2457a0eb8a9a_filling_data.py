"""filling_data

Revision ID: 2457a0eb8a9a
Revises: a787d86cf791
Create Date: 2025-12-11 15:16:48.255104

"""
import os
import sys
import uuid
import requests

from datetime import datetime
from pydantic import BaseModel
from typing import Sequence, Union
from alembic import op

from core.db.models import Video, VideoSnapshot

src_path = os.path.join(os.path.dirname(__file__), "..", "..", "src")
src_path = os.path.abspath(src_path)
sys.path.insert(0, src_path)


# revision identifiers, used by Alembic.
revision: str = '2457a0eb8a9a'
down_revision: Union[str, Sequence[str], None] = '1f9859e3d6cd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class VideoModel(BaseModel):
    id: uuid.UUID
    video_created_at: datetime
    views_count: int
    reports_count: int
    comments_count: int
    creator_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class SnapshotModel(BaseModel):
    id: uuid.UUID
    video_id: uuid.UUID
    views_count: int
    likes_count: int
    reports_count: int
    comments_count: int
    delta_views_count: int
    delta_likes_count: int
    delta_reports_count: int
    delta_comments_count: int
    created_at: datetime
    updated_at: datetime


def upgrade() -> None:
    """Upgrade schema."""
    file_id = "1BZOYxhDmMGJrSbPdcQgQjh0HRzN1YZt5"
    response = requests.get(f"https://drive.google.com/uc?export=download&id={file_id}")
    parsed_data = response.json()
    videos = []
    snapshots = []
    print("Parsing data...")
    for video in parsed_data["videos"]:
        snapshots += [SnapshotModel(**snapshot) for snapshot in video["snapshots"]]
        videos.append(VideoModel(**video))
    print("Updating database...")
    op.bulk_insert(Video.__table__, [video.model_dump(exclude_none=True) for video in videos])
    op.bulk_insert(VideoSnapshot.__table__, [snapshot.model_dump(exclude_none=True) for snapshot in snapshots])
    print("Done!")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("TRUNCATE TABLE videos CASCADE")
