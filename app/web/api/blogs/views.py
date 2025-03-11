#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: views
Time: 2025/3/6 16:05
"""
from typing import List

from fastapi import APIRouter, Depends

from app.common.request import FilterParams
from app.common.response import BaseResponse
from app.services import BlogService
from app.web.api.blogs.schema import ArticleModelInputDTO

router = APIRouter(prefix="/article")


@router.get("")
async def query_by_pagination(
    filter_query: FilterParams = Depends(FilterParams),
    blog_service: BlogService = Depends(),
):
    page_info, items = await blog_service.query_by_pagination(
        page=filter_query.page, page_size=filter_query.page_size
    )
    return BaseResponse.success(data=items, page_info=page_info)


@router.get("/{article_id}")
async def query_by_id(article_id: int, blog_service: BlogService = Depends()):
    data = await blog_service.query_one(article_id=article_id)
    return BaseResponse.success(data=data)


@router.post("")
async def create(article: ArticleModelInputDTO, blog_service: BlogService = Depends()):
    article = await blog_service.create(
        title=article.title,
        content=article.content,
        category=article.category,
        remark="",
    )
    if not article:
        return BaseResponse.error()
    return BaseResponse.success(data={"article_id": article.id})


@router.put("/{article_id}")
async def update(article_id: int, blog_service: BlogService = Depends()):
    pass


@router.put("/all")
async def update_all(article_id: int, blog_service: BlogService = Depends()):
    pass


@router.delete("/{article_id}")
async def delete(article_id: int, blog_service: BlogService = Depends()):
    pass


@router.delete("/all")
async def delete_all(article_ids: List[int], blog_service: BlogService = Depends()):
    pass
