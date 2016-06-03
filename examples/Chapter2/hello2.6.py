# coding=utf-8

from flask import Flask
# Flask扩展，使用Flask-Script支持命令行选项
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello world!</h1>'


@app.route('/user/<name>')
def user(name):
    return "<h1>hello, %s</h1>" % name


if __name__ == '__main__':
    manager.run()
