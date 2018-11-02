from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, MainShow


def home(request):# 首页
    # 轮播图数据
    wheels = Wheel.objects.all()
    # 导航数据
    navs = Nav.objects.all()
    # 每日必购
    mustbuys = Mustbuy.objects.all()
    shopList = Shop.objects.all()
    shophead = shopList[0]
    shoptab = shopList[1:3]
    shopclass = shopList[3:7]
    shopcommend = shopList[7:11]
    # 商品主体内容
    mainshows = MainShow.objects.all()
    data = {
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead': shophead,
        'shoptab': shoptab,
        'shopclass': shopclass,
        'shopcommend': shopcommend,
        'mainshows': mainshows
    }
    return render(request,'home/home.html',context=data)


def market(request):
    return render(request,'market/market.html')


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')