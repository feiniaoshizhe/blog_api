#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: views
Time: 2025/3/6 16:05
"""
from fastapi import APIRouter

from app.common.request import PageQuery
from app.common.response import BaseResponse
from app.services import blog_service

router = APIRouter()


@router.get("", response_model=BaseResponse)
async def get_blogs(page: PageQuery):
    blog_service.query()
