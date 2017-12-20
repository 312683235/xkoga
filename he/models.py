from django.db import models
from datetime import datetime

# Create your models here.
class NaviCategroy(models.Model):
    name = models.CharField(max_length=20,verbose_name='分类名称',unique=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '分类管理'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=32,verbose_name='密码')
    avatar = models.ImageField(upload_to='image/user-avatar/%Y/%m',verbose_name='头像')
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    is_active = models.CharField(choices=(('Y','激活'),('N','未激活')),max_length=2,verbose_name='激活状态',null=True,blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Code(models.Model):
    email = models.EmailField(max_length=50,verbose_name='邮箱')
    code = models.CharField(max_length=6,verbose_name='验证码')
    type = models.CharField(choices=(('register','用户注册'),('findpwd','找回密码')),max_length=12,verbose_name='验证码类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email


class Content(models.Model):
    auth = models.ForeignKey(UserInfo,to_field='username',verbose_name='作者')
    company = models.CharField(max_length=30,verbose_name='公司')
    desc = models.CharField(max_length=200,verbose_name='简介')
    tag = models.CharField(max_length=20,verbose_name='标签')
    follow = models.IntegerField(verbose_name='关注')
    click = models.IntegerField(verbose_name='点击')
    comment = models.CharField(max_length=300,verbose_name='内容')
    share = models.IntegerField(verbose_name='分享')
    content = models.CharField(max_length=8000,verbose_name='内容')
    time = models.DateTimeField(auto_now_add=True,verbose_name='时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '文章管理'
        verbose_name_plural = verbose_name


class Mechanism(models.Model):
    c_name = models.CharField(max_length=20,verbose_name='中文名称')
    e_name = models.CharField(max_length=50,verbose_name='英文名称')
    url = models.URLField(max_length=100, verbose_name='网址')
    creation_time = models.DateTimeField(verbose_name='注册时间')
    img = models.ImageField(upload_to='image/mechanism/%Y/%m',verbose_name='机构图片')
    core = models.CharField(max_length=20, verbose_name='机构总部')
    desc = models.TextField(max_length=500, verbose_name='简介')
    accept = models.CharField(max_length=20, verbose_name='受资方')
    invest = models.CharField(max_length=20, verbose_name='投资方')
    look_num = models.IntegerField(default=0,verbose_name='浏览量')
    category = models.CharField(max_length=20,verbose_name='所属行业')
    invest_time = models.DateTimeField(verbose_name='投资时间')
    content = models.TextField(max_length=8000,verbose_name='结构投资介绍')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '机构列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.c_name


class link(models.Model):
    name = models.CharField(max_length=20,verbose_name='名称')
    url = models.URLField(max_length=100, verbose_name='网址')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='创建时间')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=10,verbose_name='城市',unique=True)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Public(models.Model):
    name = models.CharField(max_length=10,verbose_name='姓名')
    email = models.EmailField(max_length=20,verbose_name='邮箱')
    mobile = models.CharField(verbose_name='电话',max_length=11)
    postion = models.CharField(max_length=10,verbose_name='职位')
    avatar = models.ImageField(upload_to='image/project-avatar/%Y/%m',verbose_name='头像')
    product_name = models.CharField(max_length=20,verbose_name='产品名称')
    weibo = models.CharField(max_length=50,verbose_name='微博',null=True,blank=True)
    url = models.URLField(max_length=100,verbose_name='网址')
    category = models.CharField(max_length=10,verbose_name='分类')
    addr = models.ForeignKey(City,to_field='name')
    run_time = models.DateTimeField(auto_now_add=True,verbose_name='产品上线时间')
    logo = models.ImageField(upload_to='image/project-logo/%Y/%m')
    desc = models.CharField(max_length=45,verbose_name='简介')
    content = models.CharField(max_length=300,verbose_name='介绍')
    tag = models.CharField(max_length=30,verbose_name='标签')
    image = models.ImageField(upload_to='image/project-image/%Y/%m')
    click_num = models.IntegerField(verbose_name='点击数量')
    follow = models.IntegerField(verbose_name='关注数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '产品发布'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.product_name


class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name='项目分类')
    c_name = models.CharField(max_length=20,verbose_name='别名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '项目分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Consultation(models.Model):
    title = models.CharField(max_length=32,verbose_name='标题')
    tag = models.CharField(max_length=20,verbose_name='关键字')
    category = models.ForeignKey(Category,verbose_name='分类')
    company = models.CharField(max_length=20,verbose_name='公司')
    desc = models.TextField(max_length=300,verbose_name='导读')
    content = models.TextField(max_length=8000,verbose_name='内容')
    follow = models.IntegerField(verbose_name='关注数量')
    share = models.IntegerField(verbose_name='分享数量')
    comment_num = models.IntegerField(verbose_name='评论数量')
    time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    click_num = models.IntegerField(verbose_name='点击数量')
    images = models.ImageField(upload_to='image/consultation/%Y/%m', verbose_name='产品图片')
    is_banner = models.BooleanField(choices=((True,'展示'),(False,'不展示')),verbose_name='是否置顶',default=False)
    city = models.ForeignKey(City, verbose_name='城市')

    class Meta:
        verbose_name = '咨询文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Server(models.Model):
    title = models.CharField(max_length=32,verbose_name='标题')
    img = models.ImageField(upload_to='image/server/%Y/%m',verbose_name='图片')
    city = models.ForeignKey(City,verbose_name='城市')
    category = models.ForeignKey(Category,verbose_name='分类')
    time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    desc = models.TextField(max_length=500,verbose_name='项目介绍')
    images = models.ImageField(upload_to='image/server/%Y/%m',verbose_name='产品图片')
    pro_data = models.TextField(max_length=500,verbose_name='数据')
    pro_capital = models.TextField(max_length=500,verbose_name='资本')
    pro_pro = models.TextField(max_length=500,verbose_name='产品')
    pro_patent = models.TextField(max_length=500,verbose_name='专利')
    pro_qua = models.TextField(max_length=500,verbose_name='资质')
    pro_other = models.TextField(max_length=500,verbose_name='其他')
    member = models.TextField(max_length=200,verbose_name='成员')
    follow = models.IntegerField(verbose_name='关注数量',default=0)
    state = models.CharField(max_length=7,choices=(('正在运营','正在运营'),('暂停运营','暂停运营')),verbose_name='运营状态')
    look_num = models.IntegerField(verbose_name='观看数量')

    class Meta:
        verbose_name = '服务文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    username = models.ForeignKey(UserInfo,to_field='username',verbose_name='用户名')
    content = models.CharField(max_length=300,verbose_name='评论内容')
    time = models.DateTimeField(default=datetime.now,verbose_name='评论时间')
    article = models.ForeignKey(Consultation,verbose_name='文章ID')

    class Meta:
        verbose_name = '评论管理'
        verbose_name_plural = verbose_name