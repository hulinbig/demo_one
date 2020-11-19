#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'

from flask import Blueprint,request,render_template,redirect
from apps.user.model import User
user_bp = Blueprint('user', __name__)


#列表保存的是一个一个的用户对象
users = []

@user_bp.route('/')
def user_center():
    return render_template('user/show.html', users=users)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        #获取post提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            #用户名唯一
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg="用户名重复，请重新输入")
            #创建user对象
            user = User(username, password, phone)
            #添加到用户列表
            users.append(user)
            return redirect('/')

    return render_template('user/register.html')

@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return '用户登陆'

@user_bp.route('/del')
def del_user():
    #交互,获取传递的username
    #查找username
    #删除username
    username = request.args.get('username')
    for user in users:
        if user.username == username:
            users.remove(user)
            # return "删除成功"
            return redirect('/')
        else:
            return "删除失败,请检查传参"

@user_bp.route('/update', methods=['GET', 'POST'], endpoint='update')
def update_user():
    if request.method == 'POST':
        relname = request.form.get('relname')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        for user in users:
            if user.username == relname:
                user.username = username
                user.phone = phone
                return redirect('/')



    if request.method == 'GET':
        username = request.args.get('username')
        for user in users:
            if user.username == username:
                #做修改的操作
                return render_template('user/update.html', user=user)



@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return '用户退出'