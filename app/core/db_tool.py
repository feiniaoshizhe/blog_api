#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: youshun xu
File: db_tool
Time: 2025/3/11 15:52
"""
from math import ceil
from typing import Union

from fastapi import Depends
from sqlalchemy import Row, select, Result, Select, Table, func, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Query

from app.common.response import PageInfo
from app.core.db import get_db_session


class BaseQuery:
    def get_page_info(self, page_size: int, page: int, total: int) -> PageInfo:
        """
        get page info
        :param page_size:
        :param page:
        :param total:
        :return:
        """
        pages = ceil(total / page_size)
        page_info = PageInfo(pages=pages, page_size=page_size, page=page, total=total)
        return page_info

    def check_model_instance(self, obj: Row) -> bool:
        return hasattr(obj, "__table__")

    def convert_all(
        self, result: list[Row], to_dict: bool = False, value_list: bool = False
    ):
        """
         Convert a list of SQLAlchemy Row objects to a desired format (list of dictionaries or list of lists).

         query = select(User.username, User.email).where(User.id.in_([1,2]))
         result = session.execute(query).all()
         print(convert_all(result, to_dict=True))
         [{'username': 'John', 'email': '<EMAIL>'}]

        :param    result: List of SQLAlchemy Row objects.
        :param     to_dict: Convert to dictionaries if True. Defaults to False.
        :param    value_list: Convert to lists of values if True. Defaults to False.
        :return:    List of dictionaries, lists, or Row objects based on the conversion settings.
        """
        if not result:
            return result
        first_row = result[0]
        objects = []
        is_model_instance = self.check_model_instance(first_row[0])
        for row in result:
            row = row[0] if is_model_instance else row
            if to_dict:
                data = row._asdict() if not is_model_instance else row.to_dict()
                objects.append(data)
            elif value_list:
                data = (
                    list(row._asdict().values())
                    if not is_model_instance
                    else list(row.to_dict().values())
                )
                objects.append(data)
            else:
                objects.append(row)
        return objects

    def convert_one(self, row: Row, to_dict: bool = False):
        """
        Convert a single SQLAlchemy Row object to a desired format (dictionary or Row object).

        query = select(User.username, User.email).where(User.id.in_([1,2]))
        result = session.execute(query).first()
        print(convert_one(result, to_dict=True))
        {'username': 'John', 'email': '<EMAIL>'}

        :param row: SQLAlchemy Row object.
        :param to_dict: Convert to dictionary if True. Defaults to False.
        :return: Dictionary or Row object based on the conversion settings.
        """
        if not row:
            return row
        is_model_instance = self.check_model_instance(row[0])
        row = row if not is_model_instance else row[0]
        if to_dict:
            return row._asdict() if not is_model_instance else row.to_dict()
        return row

    def query_to_value_list(self, query: Query) -> list[list]:
        """
        Convert SQLAlchemy Query object to a list of lists (each inner list represents a row of values).

        query = session.query(User.username, User.email).filter(User.is_active == True)
        print(query_to_value_list(query))
        [['John', '<EMAIL>']]

        :param query: SQLAlchemy Query object.
        :return: list[list]: List of lists where each inner list represents a row of values.
        """
        result = query.all()
        if not result:
            return []
        first = result[0]
        is_model_instance = self.check_model_instance(first)
        if is_model_instance:
            return [list(row.to_dict().values()) for row in result]
        else:
            return [list(v._asdict().values()) for v in result]

    def query_to_dict_list(self, query: Query) -> list[dict]:
        """
        Convert SQLAlchemy Query object to a list of dictionaries (each dictionary represents a row of data).

        query = session.query(User.username, User.email).filter(User.is_active == True)
        print(query_to_dict_list(query))
        [{'username': 'John', 'email': '<EMAIL>'}]

        :param query: SQLAlchemy Query object.
        :return:  list[dict]: List of dictionaries where each dictionary represents a row of data.
        """
        result = query.all()
        if not result:
            return []
        first = result[0]
        is_model_instance = self.check_model_instance(first)
        if is_model_instance:
            return [row.to_dict() for row in result]
        else:
            return [v._asdict() for v in result]


class AsyncQuery(BaseQuery):
    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def async_execute(self, query: select) -> Result:
        return await self.session.execute(query)

    async def fetchall(
        self, query: Select, to_dict: bool = False, value_list: bool = False
    ) -> Union[list[Row], list[dict], list[list]]:
        """
        Asynchronously fetch all results of a SQLAlchemy Select query and convert them to the desired format.

        query = select(User.username, User.email).where(User.id.in_([1,2]))
        result = await fetchall(query, to_dict=True)
        result
        [{'username': 'John', 'email': '<EMAIL>'}]

        :param query: SQLAlchemy Select query.
        :param to_dict: Convert results to dictionaries if True. Defaults to False.
        :param value_list:  Convert results to lists of values if True. Defaults to False.
        :return:   Union[list[Row], list[dict], list[list]]: List of rows in the desired format.

        """
        result = await self.async_execute(query)
        result = result.all()
        return self.convert_all(result, to_dict, value_list)

    async def fetchone(self, query: Select, to_dict: bool = False) -> Union[Row, dict]:
        """
        Asynchronously fetch the first result of a SQLAlchemy Select query and convert it to the desired format.

        Args:
            query (Select): SQLAlchemy Select query.
            to_dict (bool, optional): Convert result to dictionary if True. Defaults to False.
            _session (AsyncSession, optional): AsyncSession object to execute the query with. Defaults to None.

        Returns:
            Union[Row, dict]: First row in the desired format.

        Example:
            query = select(User.username, User.email).where(User.id.in_([1,2]))
            result = await fetchone(query, to_dict=True)
            result
            {'username': 'John', 'email': '<EMAIL>'}
        """
        result = await self.async_execute(query)
        row = result.first()
        return self.convert_one(row, to_dict)

    async def fetch_count(self, query: Select) -> int:
        """
        Asynchronously fetch the count of results for a given SQLAlchemy Select query.

        Args:
            query (Select): SQLAlchemy Select query.
            _session (AsyncSession): AsyncSession object to execute the query with.

        Returns:
            int: Count of results.

        Example:
            query = select(User.username, User.email).where(User.id.in_([1,2]))
            result = await fetch_count(query)
            result
            10
                Alternative Approach (with subquery):
            In certain cases, you may choose to use a subquery for the count. For example:

            - Original query with JOIN:
                ```sql
                SELECT id, name, email FROM users
                JOIN addresses ON addresses.user_id = users.id
                WHERE addresses.email LIKE '%@example.com';
                ```

            - count version:
                ```sql
                SELECT COUNT(1) FROM users
                  JOIN addresses ON addresses.user_id = users.id
                  WHERE addresses.email LIKE '%@example.com';
                ```
        """
        select_from = query.get_final_froms()[0]
        if isinstance(select_from, Table):
            count_query = (
                query.select_from(select_from)
                .with_only_columns(func.count(text("1")))
                .order_by(None)
            )
        else:
            count_query = query.with_only_columns(func.count(text("1"))).order_by(None)
        result = await self.async_execute(count_query)
        return result.first()[0]

    async def pagination(
        self,
        query: Select,
        page: int = 1,
        page_size: int = 10,
    ) -> tuple[PageInfo, list[dict]]:
        """
        Perform asynchronous pagination on a SQLAlchemy Select object.

         query = select(User.username, User.email).where(User.id.in_([1,2]))
         total, result = await pagination(query)
         total, result
         10, [{"username": "John", "email": "<EMAIL>"}, ...]

         query = session.query(User.username, User.email).where(User.id.in_([1, 2]))
         Pager, result = await pagination(query)
         Pager, result
         <class Pager>, [{"username": "John", "email": "<EMAIL>"}, ...]

         :param query: SQLAlchemy Select query.
         :param page: Page number. Defaults to 1.
         :param page_size: Number of results per page. Defaults to 10.
         :return:  tuple[Pager, list[dict]]: Total count of results and list of results for the requested page.
        """
        offset = (page - 1) * page_size
        total = await self.fetch_count(query)
        paginate = query.offset(offset).limit(page_size)
        result = await self.fetchall(paginate, to_dict=True)
        page_info = self.get_page_info(page_size, page, total)
        return page_info, result


class SyncQuery(BaseQuery):
    pass


database = AsyncQuery()
database_sync = SyncQuery()
