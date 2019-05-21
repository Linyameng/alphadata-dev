# -*- coding: utf-8 -*-
"""
Created on 2018/5/24

@author: xing yan
"""
from datetime import datetime
from flask import render_template, abort, flash, redirect, url_for ,session
from flask_login import login_required

from . import main
from .. import db
from ..models import Permission, User, EnvironMapping, PageView
from ..decorators import permission_required, admin_required

from ..create_execute import OracleEngine
from collections import OrderedDict


@main.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return 'For administrator'


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderate_only():
    return 'for comment moderators!'


@main.route('/user/<username>', methods=('GET',))
def user_info(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)
