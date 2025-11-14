from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def cmdb(request):
    return HttpResponse("Hello, world. You're at the cmdb.")

def asset(request, asset_id):
    return HttpResponse(f"Hello, world. You're at the asset {asset_id}.")
