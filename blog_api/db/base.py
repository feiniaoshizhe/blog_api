import datetime

from sqlalchemy import func, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from blog_api.db.meta import meta


# from blog_api.db.models.users import current_active_user


class Base(DeclarativeBase):
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
    # create_by: Mapped[str] = mapped_column(
    #     String(256), default=current_active_user.id, comment="创建人"
    # )
    # update_by: Mapped[str] = mapped_column(
    #     String(256),
    #     default=current_active_user.id,
    #     onupdate=current_active_user.id,
    #     comment="更新人",
    # )
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, comment="软删除")
