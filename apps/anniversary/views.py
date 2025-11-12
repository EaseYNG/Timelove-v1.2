from dbm import error

from django.contrib.auth.decorators import login_required
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
