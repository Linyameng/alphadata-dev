# -*- coding: utf-8 -*-
"""
Created on 2018/5/24

@author: xing yan
"""
from flask import render_template
from . import core


@core.app_errorhandler(403)
def page_not_found(e):
    return render_template('403.html'), 403


@core.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@core.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
