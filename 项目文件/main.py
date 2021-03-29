from flask import Flask, render_template, flash, redirect, url_for,session
from flask import request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from __init__ import *
from models import *

# class loginForm(FlaskForm):  # 自创表单函数
#     text = StringField('输入框:', validators=[DataRequired('啊这，你怎么不输入')])  # u用于转码
#     submit = SubmitField('提交:')


# @app.route('/form', methods=['GET', 'POST'])
# def login():
#     return render_template('index.html')
#
# app = Flask(__name__)
# app.config.from_object(Config)
# app.secret_key = '我是密码'
# db = SQLAlchemy(app)
# # db.init_app(app)



@app.route('/',methods=['GET','POST'])
def test():

    # if request.form.get('转到login')=='点我':
    #     return redirect('login')#重定向到路由
    # else:
    #     user_list=User.query.all()
    #     print(user_list.id)
        return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.form.get('isuser') == '1':
        text =request.form.get('user')
        text='卧槽'
        return redirect(url_for('index',text=text))
    else:
        return render_template('login.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.form.get('转到login')=='点我':
        return redirect('test')#重定向到路由
    else:
        user_list=User.query.all()
        print(user_list[0].id)
        return render_template('index.html',user_list=user_list)

    # if request.method == 'POST':
    #     text = request.form.get('text')
    #     flash(text)
    #     return render_template('login.html', text=text)
    #     # flash需要加密
    # str = 'sharding'
    # login_Form = loginForm()
    # i = 0
    # my_list = [1, 2, 3, 4, 5]
    # # 前面是变量名，模板中使用。后面是定义的变量
    # # my_dict={'name':潘增滢 'url'='www.xxxx.com'}
    # #        这个是字典数据
    # #        使用时用my_dict.url   my_dict['url']
    # return render_template('index.html', str=str, my_list=my_list, loginForm=login_Form)


#
# db.drop_all()
# db.create_all()
#user=User(name='123')创建对象
#db.session.add(user)加入
#db.session.add_all([1,2,4])方括号代表以列表方式提交
#db.session.commit()提交
#db.session.delete(user)删除
#db.session.submit()提交
#User.query.all()
#User.query.count()
#User.query.filter_by(id=4).first()||User.query.get(4)查询id为4
#User.query.filter(User.id==4)

# @app.route('/',defaults={'name':'sb'})
# @app.route('/<name>')
# def hello_world(name):
#    return '<h1>Hello World!%s </h1>' % name


# @app.route('/login',methods=["POST"])
# def login():
#    try:
#        data=request.get_json()
#        user_name=data.get("user_name")


#    except Exception as e:
#        print(e)


if __name__ == '__main__':

    app.run()
