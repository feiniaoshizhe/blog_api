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
    def success_response(data: Any):
        return BaseResponse(code=200, message="success", data=data)

    @staticmethod
    def error_response(code: int, message: str):
        return BaseResponse(code=code, message=message)
