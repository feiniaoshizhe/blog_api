#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: response
Time: 2025/3/6 18:36
"""

from typing import Generic, TypeVar, Optional, Any

from pydantic import BaseModel

T = TypeVar("T")


class PageInfo(BaseModel, Generic[T]):
    page: int
    page_size: int
    pages: int
    total: int


class BaseResponse(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T] = None
    page_info: PageInfo = None

    @staticmethod
    def success(
        code: int = 200,
        message: str = "success",
        data: Any = None,
        page_info: PageInfo = None,
    ):
        return BaseResponse(code=code, message=message, data=data, page_info=page_info)

    @staticmethod
    def error(code: int = 201, message: str = "failed"):
        return BaseResponse(code=code, message=message)
