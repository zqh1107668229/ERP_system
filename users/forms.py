from django import forms

# 登录验证
class RegisterForm(forms.Form):
    # required=True为必填字段,min_length=即最小长度为多少    下面的username必须跟html页面中<input name="username" 中的username相同
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=2)







