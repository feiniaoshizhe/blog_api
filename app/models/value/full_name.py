#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: full_name
Time: 2025/3/4 11:11
"""
import dataclasses


@dataclasses.dataclass
class FullName:
    # 全名
    full_name: str
    # 姓
    last_name: str | None
    # 名
    first_name: str | None
