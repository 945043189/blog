# _*_ coding: utf-8 _*_

# 调试模式是否开启
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
# session必须要设置key
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# mysql数据库连接信息,这里改为自己的账号
SQLALCHEMY_DATABASE_URI = "mysql://jira_root:zhsy_jira_20180528@127.0.0.1:23306/blog"
