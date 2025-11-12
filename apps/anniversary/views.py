from dbm import error

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Anniversary

# Create your views here.
@login_required(login_url='/login/')
def create_anniversary(request):
    current_user = request.user
    if request.method == 'GET':
        return render(request, 'anniversary_create.html')
    elif request.method == 'POST':
        _date = request.POST.get('date')
        _title = request.POST.get('title')
        _description = request.POST.get('description')
        if not _date or not _title:
            return render(request, 'anniversary_create.html', {'error': "请填写所有字段！"})
        anniversary = Anniversary.objects.create(owner=current_user, date=_date, title=_title, description=_description)
        anniversary.save()
        print("add anniversary")
        return redirect('/home/')

@login_required(login_url='/login/')
def db_display_anniversaries(request):
    return render(request, "db_objects_display.html", {'object_name': "Anniversaries", 'objects': Anniversary.objects.all()})

def get_anniversary_by_id(anniversary_id):
    return Anniversary.objects.get(id=anniversary_id)

# 获取当前用户的所有纪念日
def get_anniversaries(current_user):
    # 筛选所有属于当前用户的纪念日
    anniversaries = list(Anniversary.objects.filter(owner=current_user))
    return anniversaries

def edit_anniversary(request):
    _id = request.POST.get('id') or request.GET.get('id')
    anniversary = get_anniversary_by_id(_id)
    if request.method == 'POST':
        anniversary.date = request.POST.get('date')
        anniversary.title = request.POST.get('title')
        anniversary.description = request.POST.get('description')
        anniversary.save()
        return redirect('/home/')

    # GET 请求渲染模板
    return render(request, 'anniversary_edit.html', {'anniversary': anniversary})


