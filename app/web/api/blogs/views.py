#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: views
Time: 2025/3/6 16:05
"""

from fastapi import APIRouter, Depends

from app.common.request import FilterParams
from app.common.response import BaseResponse, PageInfo
from app.services import BlogService
from app.web.api.blogs.schema import ArticleModelInputDTO

router = APIRouter(prefix="/blogs")


@router.get("")
async def get_blogs(
    filter_query: FilterParams = Depends(FilterParams),
    blog_service: BlogService = Depends(),
):
    articles = await blog_service.query(
        limit=filter_query.limit, offset=filter_query.offset
    )
    return BaseResponse.success(data=PageInfo(items=articles))


@router.get("/{blog_id}")
async def get_blog_by_id(blog_id: int, blog_service: BlogService = Depends()):
    pass


@router.post("")
async def create_blog(
    article: ArticleModelInputDTO, blog_service: BlogService = Depends()
):
    article_id = await blog_service.create(
        title=article.title,
        content=article.content,
        category=article.category,
        remark="",
    )
    if not article_id:
        return BaseResponse.error()
    return BaseResponse.success(data={"article_id": article_id})


@router.put("/{blog_id}")
async def update_blog(blog_id: int, blog_service: BlogService = Depends()):
    pass


@router.delete("/{blog_id}")
async def delete_blog(blog_id: str, blog_service: BlogService = Depends()):
    pass
