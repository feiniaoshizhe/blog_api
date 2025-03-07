#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: response
Time: 2025/3/6 18:36
"""

from typing import Generic, TypeVar, Optional, List, Any

from pydantic import BaseModel

T = TypeVar("T")


class PageInfo(BaseModel, Generic[T]):
    page_index: int
    page_size: int
    total: int
    items: List[T]


class BaseResponse(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T] = None

    @staticmethod
    def success(code: int = 200, message: str = "success", data: Any | None = None):
        return BaseResponse(code=code, message=message, data=data)

    @staticmethod
    def error(code: int = 201, message: str = "failed"):
        return BaseResponse(code=code, message=message)
