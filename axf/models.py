from django.db import models

# Create your models here.
# 基础类
class Base(models.Model):
    # 图片
    img = models.CharField(max_length=100)
    # 名称
    name = models.CharField(max_length=100)
    # 商品编号
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract = True

# 轮播图
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'
# 导航
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'
# 每日必购
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'
#商品部分
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'
# 商品主体内容
class MainShow(models.Model):
    trackid = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=8)
    brandname = models.CharField(max_length=50)
    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=8)
    productid1 = models.CharField(max_length=8)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()
    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=8)
    productid2 = models.CharField(max_length=8)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()
    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=8)
    productid3 = models.CharField(max_length=8)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()
    class Meta:
        db_table = 'axf_mainshow'

# 商品分类
class Foodtypes(models.Model):
    typeid = models.CharField(max_length=8) # 分类ID
    typename = models.CharField(max_length=100) # 分类名称
    childtypenames = models.CharField(max_length=256)   # 子类名称
    typesort = models.IntegerField()    # 显示先后顺序
    class Meta:
        db_table = 'axf_foodtypes'

# 商品信息
class Goods(models.Model):
    productid = models.CharField(max_length=10) # 商品ID
    productimg = models.CharField(max_length=100)   # 商品图片
    productname = models.CharField(max_length=100)  # 商品名称
    productlongname = models.CharField(max_length=100)  # 商品长名称
    isxf = models.BooleanField(default=False)    # 精选
    pmdesc = models.BooleanField(default=False)  # 买一送一
    specifics = models.CharField(max_length=100)   # 规格
    price = models.DecimalField(max_digits=7, decimal_places=2)    # 价格
    marketprice = models.DecimalField(max_digits=7, decimal_places=2)  # 商场价格
    categoryid= models.IntegerField()   # 分类ID
    childcid = models.IntegerField()    # 子类ID
    childcidname = models.CharField(max_length=100) # 分类名称
    dealerid = models.CharField(max_length=10)  # 详情ID
    storenums = models.IntegerField()   # 库存
    productnum = models.IntegerField()  # 销量
    class Meta:
        db_table = 'axf_goods'

class User(models.Model):
    # 账号
    account = models.CharField(max_length=80, unique=True)
    # 密码
    password = models.CharField(max_length=256)
    # 名字
    name = models.CharField(max_length=100)
    # 手机号
    phone = models.CharField(max_length=20, unique=True)
    # 地址
    addr = models.CharField(max_length=256)
    # 头像
    img = models.CharField(max_length=100)
    # 等级
    rank = models.IntegerField(default=1)
    # token
    token = models.CharField(max_length=256)
    class Meta:
        db_table = 'axf_user'

class Cart(models.Model):
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    number = models.IntegerField()
    isselect = models.BooleanField(default=True)

    class Meta:
        db_table = 'axf_cart'
