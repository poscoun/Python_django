from django.shortcuts import render, redirect
from .models import *
from random import *
from sendEmail.views import *

# main views.py

# Create your views here.
def index(request):
    if 'user_name' in request.session.keys():
        return render(request, 'main/index.html')
    else :
        return redirect('main_signin')

def signup(request):
    return render(request, 'main/signup.html')

def signin(request):
    return render(request, 'main/signin.html')

def verifyCode(request):
    return render(request, 'main/verifyCode.html')

def verify(request):
    return redirect('main_index')

def result(request):
    return render(request, 'main/result.html')

def join(request):
    #print('request : ', request)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name=name, user_email=email, user_password = pw)
    user.save()

    # 인증 코드 생성 - 4자리 정수로 생성 - 랜덤
    code = randint(1000, 9999)
    # 쿠키에 저장
    response = redirect('main_verifyCode')
    response.set_cookie('code', code)
    response.set_cookie('user_id', user.id)

    # 인증 코드 - 이메일로 전송
    send_result = send(email, code)
    if send_result:
        return response
    else:
        return HttpResponse('이메일 발송에 실패했습니다.')
    #return response

def verify(request):
    user_code = request.POST['verifyCode']
    cookie_code = request.COOKIES.get('code')
    #print(user_code, cookie_code)

    if user_code == cookie_code:
        user = User.objects.get(id=request.COOKIES.get('user_id'))
        user.user_validate = 1
        user.save()
        response = redirect('main_index')
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        #response.set_cookie('user', user)
        request.session['user_email'] = user.user_email
        request.session['user_name'] = user.user_name

        return response
    else :
        redirect('main_verifyCode')

def logout(request):
    del request.session['user_email']
    del request.session['user_name']
    return redirect('main_signin')

def login(request):
    loginEmail = request.POST['loginEmail']
    loginPw = request.POST['loginPW']

    # 회원등록여부 체크
    try:
        user = User.objects.get(user_email=loginEmail)
    except Exception as e:
        print('e : ', e)
        return redirect('main_loginFail')

    # 비밀번호 일치 여부
    if user.user_password == loginPw:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('main_index')
    else:
        return redirect('main_loginFail')

def loginFail(request):
    return render(request, 'main/loginFail.html')










