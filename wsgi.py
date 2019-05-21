# -*- coding: utf-8 -*-
"""
Created on 2018/6/15

@author: xing yan
"""
import os
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    app.run()
