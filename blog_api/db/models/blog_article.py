#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: BlogArticle
Time: 2024/12/17 13:49
"""
from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column

from blog_api.db.base import Base


class BlogArticle(Base):
    __tablename__ = "blog_article"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        "title", String(256), nullable=False, comment="标题"
    )
    category: Mapped[str] = mapped_column(
        "category", String(256), nullable=False, comment="分类"
    )
    content: Mapped[str] = mapped_column(
        "content", Text, nullable=False, comment="内容"
    )
    traffic: Mapped[int] = mapped_column("traffic", Integer, default=1)
