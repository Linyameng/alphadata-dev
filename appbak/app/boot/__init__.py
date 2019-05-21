# -*- coding: utf-8 -*-
"""
Created on 2018/9/10

@author: xing yan
"""

from flask import Blueprint

boot = Blueprint('boot', __name__)

from . import views, errors

