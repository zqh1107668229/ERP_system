import xadmin
from xadmin import views
from .models import Supplier,Dept,Employee,StoreHouse,Dept_Supplier,ProductSpec,PriductUnit,Product,Product_Supplier


# 开启主题变换设置
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# 页头页尾
class GlobalSettings(object):
    # 页头文字
    site_title = "ERP管理系统"
    # 页尾文字
    site_footer = "版权所有：周乾浩"
    # 使页面左侧每个model收起来
    menu_style = "accordion"

class SupplierAdmin(object):
    # 显示字段
    list_display = ['supplier_id','name','address','phone','postalcode']
    # 搜索
    search_fields = ['supplier_id','name','address','phone','postalcode']
    # 过滤器
    list_filter = ['supplier_id','name','address','phone','postalcode']


class DeptAdmin(object):
    # 显示字段
    list_display = ['dept_id','name','remark']
    # 搜索
    search_fields = ['dept_id','name','remark']
    # 过滤器
    list_filter = ['dept_id','name','remark']


class EmployeeAdmin(object):
    # 显示字段
    list_display = ['employee_id','dept','name','gender','phone','birthday','address','IdentityCard']
    # 搜索
    search_fields = ['employee_id','dept','name','gender','phone','birthday','address','IdentityCard']
    # 过滤器
    list_filter = ['employee_id','dept','name','gender','phone','birthday','address','IdentityCard']


class StoreHouseAdmin(object):
    # 显示字段
    list_display = ['storehouse_id','address','phone','employee','add_time']
    # 搜索
    search_fields = ['storehouse_id','address','phone','employee','add_time']
    # 过滤器
    list_filter = ['storehouse_id','address','phone','employee','add_time']


class Dept_SupplierAdmin(object):
    # 显示字段
    list_display = ['dept_name','supplier_name']
    # 搜索
    search_fields = ['dept_name','supplier_name']
    # 过滤器
    list_filter = ['dept_name','supplier_name']


class ProductSpecAdmin(object):
    # 显示字段
    list_display = ['name','employee','remark','add_time']
    # 搜索
    search_fields = ['name','employee','remark','add_time']
    # 过滤器
    list_filter = ['name','employee','remark','add_time']


class PriductUnitAdmin(object):
    # 显示字段
    list_display = ['name','employee','remark','add_time']
    # 搜索
    search_fields = ['name','employee','remark','add_time']
    # 过滤器
    list_filter = ['name','employee','remark','add_time']


class ProductAdmin(object):
    # 显示字段
    list_display = ['product_id','name','productspec','priductunit','Price','employee','remark','add_time']
    # 搜索
    search_fields = ['product_id','name','productspec','priductunit','Price','employee','remark','add_time']
    # 过滤器
    list_filter = ['product_id','name','productspec','priductunit','Price','employee','remark','add_time']

class Product_SupplierAdmin(object):
    # 显示字段
    list_display = ['product','supplier']
    # 搜索
    search_fields = ['product','supplier']
    # 过滤器
    list_filter = ['product','supplier']


xadmin.site.register(Supplier,SupplierAdmin)
xadmin.site.register(Dept,DeptAdmin)
xadmin.site.register(Employee,EmployeeAdmin)
xadmin.site.register(StoreHouse,StoreHouseAdmin)
xadmin.site.register(Product,ProductAdmin)
xadmin.site.register(ProductSpec,ProductSpecAdmin)
xadmin.site.register(PriductUnit,PriductUnitAdmin)
xadmin.site.register(Dept_Supplier,Dept_SupplierAdmin)
xadmin.site.register(Product_Supplier,Product_SupplierAdmin)


# 主题变换class的注册
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 页头页尾class的注册
xadmin.site.register(views.CommAdminView,GlobalSettings)
