from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from he import models
from django.conf import settings
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout
from he.send_email import send_email_code
from he import froms
from datetime import datetime
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


#公共函数
def globle_setting(request):
    cookies_username = request.COOKIES.get('username')
    category = models.Category.objects.all()
    consultationlist = models.Consultation.objects.all()
    consultationshare = models.Consultation.objects.order_by('-share')
    consultationcomment = models.Consultation.objects.order_by('-comment_num')
    return {
        'globle_cookies_username':cookies_username,
        'globle_category':category,
        'globle_consultationlist':consultationlist,
        'globle_consultationshare':consultationshare,
        'globle_consultationcomment':consultationcomment,
    }


#首页
class Index(View):
    def get(self,request):
        all_link = models.link.objects.all()
        category = models.Category.objects.all()
        mechanism = models.Mechanism.objects.all()
        server_list = models.Server.objects.order_by('-id')
        consultationlist_list = models.Consultation.objects.order_by('-id')
        publiclist_list = models.Public.objects.order_by('-id')
        publiclist_follow = models.Public.objects.order_by('-follow')
        banner = models.Consultation.objects.filter(is_banner=True)
        return render(request,'index.html',{
            'all_link':all_link,
            'category':category,
            'server_list':server_list,
            'consultationlist_list':consultationlist_list,
            'publiclist_list':publiclist_list,
            'mechanism':mechanism,
            'publiclist_follow':publiclist_follow,
            'banner':banner,
        })


#公共页面
class Base(View):
    def get(self,request):
        return render(request, 'base.html')


#注册页面
class Register(View):
    def get(self,request):
        register_froms = froms.RegitserModelForm()
        return render(request,'register.html',{'register_froms':register_froms})
    def post(self,request):
        register_froms = froms.RegitserModelForm(request.POST)
        if register_froms.is_valid():
            username = register_froms.cleaned_data['username']
            password = register_froms.cleaned_data['password']
            email = register_froms.cleaned_data['email']
            avatar = request.FILES.get('file')
            password2 = request.POST.get('pwd2')
            code = request.POST.get('code')
            codeverif = models.Code.objects.get(code=code,email=email)
            if codeverif:
                if password == password2:
                    user = models.UserInfo()
                    user.username = username
                    user.password = make_password(password)
                    user.email = email
                    user.avatar = avatar
                    user.is_active = 'Y'
                    user.save()
                    #return render(request, 'index.html',{'avatar':avatar})
                    return HttpResponse('{"status":"sucess","msg":"注册成功"}',content_type='application/json')
                else:
                    #return render(request, 'register1.html', {'msg': '密码不一致'})
                    return HttpResponse('{"status":"pwderror","msg":"密码不一致"}', content_type='application/json')
            else:
                #return HttpResponse('验证码错误')
                return HttpResponse('{"status":"codeerror","msg":"验证码错误"}', content_type='application/json')
        else:
            return render(request, 'register.html', {'register_froms': register_froms})


#注册验证
class RegisterVerif(View):
    def post(self,request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        Muser = models.UserInfo.objects.filter(username=username)
        Memail = models.UserInfo.objects.filter(email=email)
        if Muser:
            return HttpResponse('{"status":"fali","msg":"用户名已存在"}',content_type='application/json')
        elif username == '':
            return HttpResponse('{"status":"usernone","msg":"请填写用户名"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"sucess","msg":"用户名可以使用"}',content_type='application/json')


#邮件发送
class SendEmail(View):
    def post(self,request):
        email = request.POST.get('email')
        if email:
            send_email_code(email,'register')
            return HttpResponse('{"status":"succees","msg":"发送成功"}',content_type='application/json')
        else:
            return HttpResponse('{"status":"fali","msg":"请填写邮箱"}',content_type='application/json')


#登录页面
class LoginView(View):
    def get(self,request):
        category = models.Category.objects.all()

        return render(request,'login.html',{'category':category})
    def post(self,request):
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        userinfo = models.UserInfo.objects.filter(username=username).first()
        check_pwd = check_password(pwd, userinfo.password)
        if userinfo and check_pwd:
            if userinfo.is_active == 'Y':
                response = HttpResponseRedirect('/index/')
                response.set_cookie('username',username)
                return response
            else:
                return HttpResponse('账号未激活')
        else:
            return render(request,'login.html',{'msg':'用户名不存在或密码错误'})


#注销用户
class Logout(View):
    def get(self,request):
        response = HttpResponseRedirect('/index/')
        response.delete_cookie('username')
        return response


#用户信息
class Userinfo(View):
    def get(self,request):
        cookies_username = request.COOKIES.get('username')
        if cookies_username:
            userinfo = models.UserInfo.objects.filter(username=cookies_username).first()
            return render(request,'userinfo.html',{'userinfo':userinfo,'cookies_username':cookies_username})


#用户修改
class Edit(View):
    def get(self,request,uid):
        if username == uid:
            userinfo = models.UserInfo.objects.filter(username=uid).first()
            return render(request,'edit.html',{'userinfo':userinfo,'uid':uid})
    def post(self,request,uid):
        cookies_username = request.COOKIES.get('username')
        if cookies_username:
            userinfo = models.UserInfo.objects.filter(username=uid).first()
            edit_froms = froms.EditModelForm(request.POST,instance=userinfo)
            if edit_froms.is_valid():
                edit_froms.save()
                return render(request, 'userinfo.html',{'userinfo':userinfo,'cookies_username':cookies_username})
            else:
                return HttpResponse('修改失败')


#发布项目详情页
class Publish(View):
    def get(self,request):
        cookies_username = request.COOKIES.get('username')
        if cookies_username:
            city = models.City.objects.all()
            return render(request,'xm_write.html',{'city':city,'cookies_username':cookies_username})
        else:
            return render(request,'login.html')

    def post(self,request):
        cookies_username = request.COOKIES.get('username')
        if cookies_username:
            project_from = froms.PublicModelForm(request.POST,request.FILES)
            if project_from.is_valid():
                project_from.save()
                return render(request,'success.html')
            else:
                print(project_from.errors)
                return render(request, 'xm_write.html',{'project_from':project_from,'cookies_username':cookies_username})
        else:
            return render(request,'login.html')


#项目列表页
class PublicList(View):
    def get(self,request):
        list = models.Public.objects.all()
        city = models.City.objects.all()
        city_id = request.GET.get('city','')
        if city_id:
            list = models.Public.objects.filter(addr_id=city_id)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(list, 3, request=request)
        results = p.page(page)

        return render(request,'publiclist.html',{'list':results,'city':city})


    def post(self,request):
        search = request.POST.get('search')
        if search:
            list = models.Public.objects.filter(product_name=search)
        return render(request,'publiclist.html',{'list':list})


#项目详情页
class Public(View):
    def get(self,request,nid):
        res = models.Public.objects.get(id=nid)
        res.click_num += 1
        res.save()
        public = models.Public.objects.filter(id=nid)
        return render(request,'public.html',{'public':public})


#投资机构详情页
class Mechanism(View):
    def get(self,request,nid):
        mechanism = models.Mechanism.objects.filter(id=nid)
        if mechanism:
            return render(request,'mechanism.html',{'mechanism':mechanism})
        else:
            return render(request, 'mechanism.html', {'mechanism': mechanism})


#投资机构列表页
class MechanismList(View):
    def get(self,request):
        news = request.GET.get('news')
        category = request.GET.get('category')
        mechanism_name = request.GET.get('mechanism-name')
        mechanismlist = models.Mechanism.objects.all()
        if news:
            mechanismlist = models.Mechanism.objects.filter(id=int(news))
        if category:
            mechanismlist = models.Mechanism.objects.filter(category=category)
        if mechanism_name:
            mechanismlist = models.Mechanism.objects.filter(c_name=mechanism_name)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(mechanismlist, 3, request=request)
        results = p.page(page)


        return render(request, 'mechanismlist.html', {'mechanismlist': results})


#创新咨询详情页
class Consultation(View):
    def get(self,request,nid):
        res = models.Consultation.objects.get(id=nid)
        res.click_num += 1
        res.save()
        consul = models.Consultation.objects.filter(id=nid)
        category = models.Category.objects.all()
        comment = models.Comment.objects.filter(article=nid)
        comment_num = models.Comment.objects.filter(article=nid).count()
        return render(request,'consultation.html',{'consul':consul,'category':category,'comment':comment,'comment_num':comment_num})


#创新咨询列表页
class ConsultationList(View):
    def get(self,request):
        consul = models.Consultation.objects.all()
        category = models.Category.objects.all()
        #分页函数
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(consul,5,request=request)
        results = p.page(page)
        return render(request,'consultaionlist.html',{'consul':results,'category':category})


# 创新咨询评论
class Comment(View):
    def post(self,request):
        is_user = request.COOKIES.get('username')
        article_id = request.POST.get('artcile_id')
        print(article_id)
        if is_user:
            comm = models.Comment()
            consulcomment = request.POST.get('consulcomment')
            comm.username_id = is_user
            comm.content = consulcomment
            comm.article_id = article_id
            comm.save()
            return HttpResponseRedirect('/consultation-{0}/'.format(article_id))
        else:
            return HttpResponse('请登录后评论')


#创新服务详情页
class Server(View):
    def get(self,request,nid):
        res = models.Server.objects.get(id=nid)
        res.look_num += 1
        res.save()
        category = models.Category.objects.all()
        sers = models.Server.objects.filter(id=nid)
        return render(request,'server.html',{'category':category,'sers':sers})


#创新服务列表页
class ServerList(View):
    def get(self,request):
        category = models.Category.objects.all()
        sers = models.Server.objects.all()
        city = models.City.objects.all()
        city_id = request.GET.get('city')
        if city_id:
            sers = models.Server.objects.filter(city_id = city_id)

        # 分页函数
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(sers, 3, request=request)
        results = p.page(page)


        return render(request,'serverlist.html',{'category':category,'sers':results,'city':city})