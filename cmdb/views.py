from django.shortcuts import render, HttpResponse, redirect
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Host
from .form import HostForm
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    hosts = Host.objects.all()
    return render(request, "main.html", {"host_list": hosts})

@login_required
def add(request):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HostForm()
    return render(request, "add.html", {'form': form})

@login_required
def edit(request, pk):
    host = Host.objects.get(pk=pk)
    if request.method == 'POST':
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HostForm(instance=host)
    return render(request, "edit.html", {'form': form, 'host': host})

@login_required
@require_POST
def delete(request, pk):
    host = Host.objects.get(pk=pk)
    host.delete()
    return redirect('index')

@csrf_exempt
def collect(request):
    """
    资产采集接口
    :param request:
    字典格式为：
    {
        "hostname": "host1",
        "ip": "192.168.1.1",
        "cpu": "Intel Xeon E5-2650",
        "mem": "128GB",
        "disk": "1TB SSD",
        "desc": "web server"
    }
    :return:
    """
    asset_info = json.loads(request.body)
    print("客户端上传字典:", asset_info)
    if request.method == 'POST':
        hostname = asset_info.get('hostname')
        ip = asset_info.get('ip')
        cpu = asset_info.get('cpu')
        mem = asset_info.get('mem')
        disk = asset_info.get('disk')
        desc = asset_info.get('desc')
        try:
            host = Host.objects.get(hostname=hostname)
        except Host.DoesNotExist:
            host = Host()
        host.hostname = hostname
        host.ip = ip
        host.cpu = cpu
        host.mem = mem
        host.disk = disk
        host.desc = desc
        host.save()
    return HttpResponse("success")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')

def test_template(request):
    """测试模板加载功能"""
    from django.template.loader import get_template
    try:
        template = get_template('edit.html')
        return HttpResponse('Template found: edit.html')
    except Exception as e:
        return HttpResponse(f'Error: {str(e)}')