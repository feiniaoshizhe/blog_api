#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: BlogArticle
Time: 2024/12/17 13:49
"""
from typing import List

from sqlalchemy import String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from blog_api.db.base import Base
from blog_api.db.models.blog.blog_comment import BlogComment


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
    traffic: Mapped[int] = mapped_column(
        "traffic", Integer, default=1, comment="访问量"
    )
    comment_num: Mapped[int] = mapped_column(
        "comment_num", Integer, default=0, comment="评论数"
    )
    remark: Mapped[str] = mapped_column(
        "remark", String(256), nullable=True, comment="备注"
    )
    comments: Mapped[List[BlogComment]] = relationship()
