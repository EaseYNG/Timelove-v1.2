from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

from .models import User


# Create your views here.
@csrf_exempt
def create_user(request):
    if request.method == 'GET':
        return render(request, "accounts_signup.html")
    if request.method == 'POST':
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        _sex = request.POST.get('sex')
        if not _username or not _password or not _sex:
            return render(request, "accounts_signup.html", {
                'error': "请填写所有字段！"
            })
        User.objects.create_user(username=_username, password=_password, sex=_sex)  # 使用密文创建
        return render(request, "accounts_create.html", {'username': _username})


@csrf_exempt
def login(request):
    # 提交GET请求时显示登录页面
    if request.method == 'GET':
        return render(request, "accounts_login.html")
    # 提交POST请求时，说明需要登录
    _username = request.POST.get('username')
    _password = request.POST.get('password')
    current_user = auth.authenticate(username=_username, password=_password)
    if not current_user:
        print("登录失败！")
        return redirect('/login/') # 输入为空则重定向
    auth.login(request, current_user) # 登录
    print("Login success")
    return redirect('/home/') # 登录成功重定向至home页



@login_required(login_url='/login/')
def logout(request):
    print("Logout success")
    auth.logout(request)
    return redirect('/login/')


def display_users(request):
    return render(request, "db_objects_display.html", {'objects': User.objects.all(), 'object_name': "All Users"})