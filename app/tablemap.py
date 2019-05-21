# -*- coding: utf-8 -*-
"""
Created on 2018/6/13

@author: xing yan
"""
from sqlalchemy import Table
from collections import OrderedDict


def tab_metadata(tab_map, metadata):
    tables = []
    for tab in tab_map:
        tables.append(Table(tab, metadata, autoload=True))
    return OrderedDict([(tab.description, tab) for tab in tables])
