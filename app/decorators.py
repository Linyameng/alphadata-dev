# -*- coding: utf-8 -*-
"""
Created on 2018/5/29

@author: xing yan
"""
from functools import wraps
from flask import abort, g, request
from flask_login import current_user
from .models import Permission, PageView
from . import db


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)


def page_views(fn):
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        page_view = PageView.query.filter_by(view=fn.__name__).first()
        if page_view is None:
            page_view = PageView(view=fn.__name__)
            db.session.add(page_view)
        if request.method == 'POST':
            page_view.pv += 1
            db.session.add(page_view)
        g.page_view = page_view
        return fn(*args, **kwargs)
    return decorated_function
