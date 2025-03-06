#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: request
Time: 2025/3/6 19:01
"""
from pydantic import BaseModel


class PageQuery(BaseModel):
    page_index: int = 0
    page_size: int = 10
