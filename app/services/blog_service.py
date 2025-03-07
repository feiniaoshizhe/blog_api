#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: blog_services
Time: 2025/3/6 18:45
"""
from typing import List, overload

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db_session
from app.models.blog.blog_article import BlogArticle


class BlogService:

    def __init__(self, session: AsyncSession = Depends(get_db_session)) -> None:
        self.session = session

    @overload
    async def query(self, blog_id: int) -> BlogArticle:
        pass

    async def query(self, limit: int = 10, offset: int = 0) -> List[BlogArticle]:
        stmt = select(BlogArticle).limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        articles = result.scalars().fetchall()
        return list(articles)

    async def create(
        self, title: str, category: str, content: str, remark: str
    ) -> int | None:
        """
        create article entity
        :param title:
        :param category:
        :param content:
        :param remark:
        :return:blog article id
        """
        entity = BlogArticle(
            title=title, category=category, content=content, remark=remark
        )
        try:
            self.session.add(entity)
            await self.session.commit()
            await self.session.flush()
        except Exception as e:
            await self.session.rollback()
            return None
        return entity.id

    def update(self):
        pass

    def delete(self):
        pass
