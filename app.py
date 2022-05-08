#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site :
# @Describe:

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
class Config(object):
    DEBUG = True
    SECRET_KEY = "root"
    # 数据库链接配置 = 数据库名称://登录账号:登录密码@数据库主机IP:数据库访问端口/数据库名称?charset=编码类型
    #SQLALCHEMY_DATABASE_URI = "mysql://root:12345678@120.46.177.150:3306/project1?charset=utf8"
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost:3306/mood?charset=utf8"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['JSON_AS_ASCII'] = False
    db=SQLAlchemy()
    # with app.app_context():
    #    db.init_app(app)
    db.init_app(app)
    return app

app = create_app(Config)

'''
定义了3个网址，用同一套模板渲染
'''
@app.route('/')
def index():
    
    from data import SourceData
    # 新建一个实例
    data = SourceData()
    # 传入一个实例，和实例的标题
    return render_template('index.html', form=data, title=data.title)

@app.route('/mood')
def mood():

    from data_mood import MoodData
    data = MoodData()
    return render_template('index.html', form=data, title=data.title)



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
