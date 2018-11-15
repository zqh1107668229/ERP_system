from django.apps import AppConfig

class JinhuoConfig(AppConfig):
    name = 'jinhuo'
    # 加上这句话，然后去__init__文件下再去配置一句话就完成xadmin左侧models名称修改
    verbose_name = "进货管理"
