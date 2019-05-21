# -*- coding: utf-8 -*-
"""
Created on 2018/7/23

@author: xing yan
"""
from flask import Blueprint

core = Blueprint('core', __name__)

from . import views, errors
