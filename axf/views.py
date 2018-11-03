from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from axf.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


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


def market(request,categoryid,childid,sortid):
    # 分类信息
    foodtypes = Foodtypes.objects.all()
    # 分类 点击 下标  >>>>  分类ID
    typeIndex = int(request.COOKIES.get('typeIndex', 0))
    # 根据分类下标 获取 对应 分类ID
    categoryid = foodtypes[typeIndex].typeid
    # 子类信息
    childtypenames = foodtypes.get(typeid=categoryid).childtypenames
    # 将每个子类拆分出来
    childTypleList = []
    for item in childtypenames.split('#'):
        arr = item.split(':')
        dir = {
            'childname':arr[0],# 子类名称
            'childid':arr[1]  # 子类ID
        }
        childTypleList.append(dir)
    # 商品信息 - 根据分类id获取对应数据
    # goodsList = Goods.objects.all()[0:5]
    if childid == '0':  # 全部分类
        goodsList = Goods.objects.filter(categoryid=categoryid)
    else:# 分类 下 子类
        goodsList = Goods.objects.filter(categoryid=categoryid,childcid=childid)

    # 排序
    if sortid == '1':# 销量排序
        goodsList = goodsList.order_by('-productnum')
    elif sortid == '2':  # 价格最低
        goodsList = goodsList.order_by('price')
    elif sortid == '3':  # 价格最高
        goodsList = goodsList.order_by(('-price'))

    data = {
        'foodtypes': foodtypes, # 分类信息
        'goodsList': goodsList,# 商品信息
        'childTypleList': childTypleList,  # 子类信息
        'categoryid':categoryid, # 分类ID
        'childid': childid,  # 子类ID
    }
    return render(request,'market/market.html',context=data)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')