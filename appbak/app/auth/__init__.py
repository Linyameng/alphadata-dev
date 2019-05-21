# -*- coding: utf-8 -*-
"""
Created on 2018/5/25

@author: xing yan
"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
