#!FlaskWebExample/venv/bin/python
#-*- coding: utf-8 -*-
#coding=utf-8

"""
第二章重点
1.
所有的Flask程序都必须创建一个程序实例。Web服务器使用一种名为Web服务器网关接口（web serve gateway interface,WSGI）的协议，
把接收自客户端的所有请求都转交这个对象处理。

2.路由
    客户端（例如 web浏览器）把请求发送给web服务器，web服务器在把请求发送给Flask程序实例。程序实例需要知道
对每个url请求运行那些大妈，所以保存了一个url到Python函数的映射关系。处理url和函数之间关系的程序称为路由。
2-1.在flask程序中定义路由最简单方式，是使用程序实例提供的app.route修饰器，把修饰的函数注册为路由。
2-2.像修饰器下的index（）函数称为视图函数（view function）。视图函数的返回值称为响应。

3.程序和和请求上下文
    关于上下文的理解可以参考知乎的回答 https://www.zhihu.com/question/26387327

4.请求调度和请求钩子

5.响应

"""""
# 实在没找到其它好办法，只能强行转码 =。=
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 导入flask模块
from flask import Flask

#导入响应函数make_response
from flask import make_response
from flask import redirect
from flask import abort

# 导入request模块
from flask import request

# 初始flask程序实例
app = Flask(__name__)


# 使用修饰器声明路由
@app.route('/')
# 视图函数
def index():
    # 调用请求对象获取请求上下文
    user_agent = request.headers.get('User-Agent')
    #
    response = make_response('<h1>HelloWorld!</h1><p>Your browser is %s.</p><p>This Response was make by make_response</p>' % user_agent, )
    response.set_cookie('answer', '42')
    return response,


# 动态url
@app.route('/user/<name>')
def user(name):
    if not name:
        return abort(404)
    return '<h1>hello, %s!</h1>' % name



if __name__ == '__main__':
    app.run(debug=True)
