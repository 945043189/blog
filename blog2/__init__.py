# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建项目对象
app = Flask(__name__)
# import  os
# print os.environ.keys()
# print os.environ.get('FLASKR_SETTINGS')
# 加载配置文件内容
app.config.from_object('blog2.setting')  # 模块下的setting文件名，不用加py后缀
app.config.from_envvar('FLASKR_SETTINGS')  # 环境变量，指向配置文件setting的路径

# 创建数据库对象
db = SQLAlchemy(app)

# 只有在app对象之后声明，用于导入model否则无法创建表，此2行要放db定义之后，同java不一样
from blog2.model import User
from blog2.model import Category
from blog2.controller import blog_message

# 引用包
from flask_login import LoginManager

# 登陆管理
# 声明login对象
login_manager = LoginManager()
# 初始化绑定到应用
login_manager.init_app(app)

# 声明默认视图函数为login，当我们进行@require_login时，如果没登陆会自动跳到该视图函数处理
login_manager.login_view = "login"


# 当登陆成功后，该函数会自动从会话中存储的用户 ID 重新加载用户对象。它应该接受一个用户的 unicode ID 作为参数，并且返回相应的用户对象。
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))
