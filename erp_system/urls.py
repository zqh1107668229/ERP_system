"""erp_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import xadmin
# 用于主页显示
from django.views.generic import TemplateView
from users.views import RegisterView
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 配置首页url
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
]
