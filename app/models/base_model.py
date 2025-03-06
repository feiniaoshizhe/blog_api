import datetime

from sqlalchemy import func, DateTime, Boolean, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.models.meta import meta


# from app.db.models.users import current_active_user


class BaseModel(DeclarativeBase):
    """Base for all models."""

    metadata = meta

    create_time: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), comment="创建时间"
    )
    update_time: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        comment="更新时间",
    )
    create_by: Mapped[str] = mapped_column(String(256), default=0, comment="创建人")
    update_by: Mapped[str] = mapped_column(
        String(256),
        default=0,
        comment="更新人",
    )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, comment="软删除")
