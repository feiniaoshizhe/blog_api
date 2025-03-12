#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: request
Time: 2025/3/6 19:01
"""
from typing import Literal


class PaginationQueryParams:
    def __init__(
        self,
        page: int = 1,
        page_size: int = 10,
        order_by: Literal["created_at", "update_at"] = "created_at",
        keys: str | None = None,
    ):
        self.page = page
        self.page_size = page_size
        self.order_by = order_by
        self.keys = (keys or "").split(",")
