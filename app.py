from blog2 import app
'''
    参考 Flask框架的学习与实战（二）：实战小项目(https://www.cnblogs.com/mysql-dba/p/6070258.html)
    示例已经跑通
'''

@app.route('/')
def hello_world():
    return 'Hello World zaj blog!'


if __name__ == '__main__':
    app.run(debug=True)
