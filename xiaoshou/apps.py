from django.apps import AppConfig


class XiaoshouConfig(AppConfig):
    name = 'xiaoshou'
    # 加上这句话，然后去__init__文件下再去配置一句话就完成xadmin左侧models名称修改
    verbose_name = "销售管理"
