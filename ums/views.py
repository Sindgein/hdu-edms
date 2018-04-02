from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404, StreamingHttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .utils import token_confirm, send_email
from .models import Teacher
# Create your views here.


@csrf_exempt
def account_signin(request):
    context = {
        'username': '',
        'password': '',
        'message': '',
    }
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/edms/')
        else:
            context['message'] = '密码错误或用户未激活'
        context['username'] = request.POST['username']
        context['password'] = request.POST['password']
    return render(request, 'users/login.html', context=context)


@csrf_exempt
def account_register(request):
    context = {
        'username': '',
        'teacher_id': '',
        'email': '',
        'password': '',
        'message': '',
    }
    if request.method == 'POST':
        username = request.POST['teacher_id']
        email = request.POST['email']
        password = request.POST['password']
        exist_username = [user.username for user in User.objects.all()]
        exist_email = [user.email for user in User.objects.all()]

        if username in exist_username:
            context['message'] = '工号 %s 已经被注册' % username
            context['teacher_id'] = request.POST['teacher_id']
            context['username'] = request.POST['username']
            context['password'] = request.POST['password']
            context['email'] = request.POST['email']
        elif email in exist_email:
            context['message'] = '邮箱 %s 已经被注册' % email
            context['teacher_id'] = request.POST['teacher_id']
            context['username'] = request.POST['username']
            context['password'] = request.POST['password']
            context['email'] = request.POST['email']
        else:
            # User.objects.create_user(username,email=email,password=request.POST['password'])
            user = User(username=username, email=email)
            user.set_password(password)
            user.is_active = False
            user.save()
            teacher = Teacher(user=user,name=request.POST['username'])
            teacher.save()
            token = token_confirm.generate_validate_token(user.username)
            message = '\n'.join(['亲爱的' + user.username + '，您好！', '欢迎加入云将科技，请访问以下链接以完成注册验证：',
                                 'http://localhost:8000/user/active/' + token])
            send_email(user.email, message)
            return HttpResponse('注册成功,请到注册邮箱中完成用户验证')
    return render(request, 'users/register.html', context=context)


def account_active(request,token):
    try:
        username = token_confirm.confirm_validate_token(token)
    except:
        username = token_confirm.remove_validate_token(token)
        user = User.objects.get(username=username)
        user.delete()
        return HttpResponse( u'对不起，验证链接已经过期，请重新<a href=\"/user/register\">注册</a>')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse(u"对不起，您所验证的用户不存在，请重新注册")
    user.is_active = True
    user.save()
    message = u'验证成功，请进行<a href=\"user/login/\">登录</a>操作'
    return HttpResponse(message)