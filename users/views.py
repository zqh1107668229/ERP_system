from django.shortcuts import render
# django基础View
from django.views.generic.base import View
# django自带user表
from django.contrib.auth.models import User
from .forms import RegisterForm
# 明文转密文模块
from django.contrib.auth.hashers import make_password
# Create your views here.

class RegisterView(View):
    # @csrf_protect
    def get(self,request):
        # register_form = RegisterForm()
        return render(request,"register.html")

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("username","")
            if User.objects.filter(username=user_name):
                return render(request,"register.html",{"register_form":register_form,"msg1":"用户已经注册"})
            pass_word = request.POST.get("password","")
            pass_word_two = request.POST.get("password_two","")
            if not pass_word == pass_word_two:
                return render(request,"register.html",{"register_form":register_form,"msg2":"两次密码不相同"})
            user_profile = User()
            user_profile.username = user_name
            user_profile.password = make_password(pass_word)
            user_profile.is_superuser = 1
            user_profile.is_staff = 1
            user_profile.save()
            return render(request,"index.html")



