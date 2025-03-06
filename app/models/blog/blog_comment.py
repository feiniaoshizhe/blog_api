#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: article_comment
Time: 2025/1/6 14:41
"""
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel


class BlogComment(BaseModel):
    __tablename__ = "blog_comment"

    id: Mapped[int] = mapped_column(primary_key=True, comment="主键")
    comment: Mapped[str] = mapped_column(
        "comment", Text, nullable=False, comment="评论"
    )
    blog_id: Mapped[int] = mapped_column(ForeignKey("blog_article.id"))
