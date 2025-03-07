#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: request
Time: 2025/3/6 19:01
"""
from typing import Literal


class FilterParams:
    def __init__(
        self,
        offset: int = 1,
        limit: int = 10,
        order_by: Literal["created_at", "update_at"] = "created_at",
        keys: str | None = None,
    ):
        self.offset = offset
        self.limit = limit
        self.order_by = order_by
        self.keys = (keys or "").split(",")
