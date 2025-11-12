from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from apps.anniversary import views
from apps.anniversary.models import Anniversary
from apps.anniversary.views import get_anniversaries, get_anniversary_by_id


# Create your views here.
@login_required(login_url='/login/')
def home(request):
    # 读取用户数据
    current_user = request.user
    name = current_user.username
    anniversaries = get_anniversaries(current_user)

    return render(request, "home.html", {'username': name, 'anniversaries': anniversaries})


def to_edit_anniversary(request):
    if request.method == 'GET':
        _id = request.GET.get('id')
        anniversary = get_anniversary_by_id(_id)
        return render(request, "anniversary_edit.html", {'anniversary': anniversary})


