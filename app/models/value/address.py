#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: address
Time: 2025/3/4 11:12
"""
import dataclasses


@dataclasses.dataclass
class Address:
    # 国
    country: str
    # 省份
    province: str
    # 市
    city: str
    # 区
    district: str | None
    # 完整地址
    address: str
