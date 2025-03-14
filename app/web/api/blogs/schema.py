#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: schema
Time: 2025/3/6 18:27
"""
from pydantic import BaseModel, ConfigDict, Field


class ArticleModelInputDTO(BaseModel):
    title: str = Field()
    category: str = Field()
    content: str = Field()

    model_config = ConfigDict(from_attributes=True)
