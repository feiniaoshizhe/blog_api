#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: blog_services
Time: 2025/3/6 18:45
"""
from typing import List

from fastapi import Depends
from sqlalchemy import select, desc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.response import PageInfo
from app.core.db import get_db_session
from app.core.db_tool import AsyncQuery
from app.models.blog.blog_article import BlogArticle


class BlogService:

    def __init__(
        self,
        session: AsyncSession = Depends(get_db_session),
        database: AsyncQuery = Depends(),
    ) -> None:
        self.session = session
        self.database = database

    @staticmethod
    async def query(article_id: int = None):
        select_row = [
            BlogArticle.id.label("article_id"),
            BlogArticle.title,
            BlogArticle.remark,
            BlogArticle.traffic,
        ]
        where = [BlogArticle.is_deleted == 0]
        order_by = [desc(BlogArticle.create_time)]
        if article_id:
            where.append(BlogArticle.id == article_id)
        query = select(*select_row).where(*where).order_by(*order_by)
        return query

    async def query_one(self, article_id: int) -> BlogArticle | None:
        query = await self.query(article_id=article_id)
        result = await self.session.execute(query)
        article = result.scalars().one_or_none()
        return article

    async def query_by_pagination(
        self, page_size: int = 10, page: int = 1
    ) -> (PageInfo, List):
        """

        :param page_size:
        :param page:
        :return:
        """
        query = await self.query()

        page_info, result = await self.database.pagination(
            query=query, page=page, page_size=page_size
        )
        return page_info, result

    async def create(
        self, title: str, category: str, content: str, remark: str
    ) -> BlogArticle | None:
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
        except SQLAlchemyError as e:
            await self.session.rollback()
            return None
        return entity

    async def update(self, article_id: int) -> BlogArticle | None:
        """
        update article
        :param article_id:
        :return:
        """
        article = await self.query_one(article_id)
        if not article:
            return None
        try:
            await self.session.commit()
            await self.session.flush()
        except SQLAlchemyError as e:
            await self.session.rollback()
        return article

    async def delete(self, article_id: int) -> bool:
        """
        soft delete article by article id
        :param article_id:
        :return:
        """
        article = await self.query_one(article_id)
        if not article:
            return False
        article.is_deleted = True
        try:
            await self.session.commit()
            await self.session.flush()
        except SQLAlchemyError as e:
            await self.session.rollback()
            return False
        return True
