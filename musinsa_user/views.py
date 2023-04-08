from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm, LoginForm
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            user_form = UserForm
            return render(request, 'musinsa_user/signup.html', {'user_form': user_form})
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)

        if password != password2:
            print("비밀번호가 다릅니다.")
            return redirect('/sign-up')
        else:
            me = get_user_model().objects.filter(username=username)  # get방식으로 조회를 하면 유저가 없을 시 오류!
            if me:
                print("이미 존재하는 아이디 입니다.")
                return redirect('/sign-up')
            else:
                UserModel.objects.create_user(username=username, password=password)
                login_form = LoginForm()
                return redirect('/sign-in', {'login_form': login_form})


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)  # 장고의 암호화된 비밀번호 확인
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/sign-in')
    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            login_form = LoginForm()
            return render(request, 'musinsa_user/signin.html', {'login_form': login_form})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
