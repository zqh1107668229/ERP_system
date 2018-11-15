import xadmin
from .models import Customer,SaleOrder,SaleOrder_Detail,Buy,Buy_Detail,Sale,Sale_Detail

class CustomerAdmin(object):
    # 显示字段
    list_display = ['customer_id','name','address','phone','PostalCode']
    # 搜索
    search_fields = ['customer_id','name','address','phone','PostalCode']
    # 过滤器
    list_filter = ['customer_id','name','address','phone','PostalCode']


class SaleOrderAdmin(object):
    # 显示字段
    list_display = ['saleorder_id','writedate','insuredate','enddate','dept','supplier','employee']
    # 搜索
    search_fields = ['saleorder_id','writedate','insuredate','enddate','dept','supplier','employee']
    # 过滤器
    list_filter = ['saleorder_id','writedate','insuredate','enddate','dept','supplier','employee']


class SaleOrder_DetailAdmin(object):
    # 显示字段
    list_display = ['saleorder_id','product_id','quantity','peice']
    # 搜索
    search_fields = ['saleorder_id','product_id','quantity','peice']
    # 过滤器
    list_filter = ['saleorder_id','product_id','quantity','peice']


class BuyAdmin(object):
    # 显示字段
    list_display = ['buy_id','comedate','dept','employee']
    # 搜索
    search_fields = ['buy_id','comedate','dept','employee']
    # 过滤器
    list_filter = ['buy_id','comedate','dept','employee']


class Buy_DetailAdmin(object):
    # 显示字段
    list_display = ['buy_id','product_id','buyorder_id','quantity','peice']
    # 搜索
    search_fields = ['buy_id','product_id','buyorder_id','quantity','peice']
    # 过滤器
    list_filter = ['buy_id','product_id','buyorder_id','quantity','peice']


class SaleAdmin(object):
    # 显示字段
    list_display = ['sale_id','saledate','dept','employee']
    # 搜索
    search_fields = ['sale_id','saledate','dept','employee']
    # 过滤器
    list_filter = ['sale_id','saledate','dept','employee']


class Sale_DetailAdmin(object):
    # 显示字段
    list_display = ['sale_id','product_id','buyorder_id','quantity','peice','discount']
    # 搜索
    search_fields = ['sale_id','product_id','buyorder_id','quantity','peice','discount']
    # 过滤器
    list_filter = ['sale_id','product_id','buyorder_id','quantity','peice','discount']


xadmin.site.register(Customer,CustomerAdmin)
xadmin.site.register(SaleOrder,SaleOrderAdmin)
xadmin.site.register(SaleOrder_Detail,SaleOrder_DetailAdmin)
xadmin.site.register(Buy,BuyAdmin)
xadmin.site.register(Buy_Detail,Buy_DetailAdmin)
xadmin.site.register(Sale,SaleAdmin)
xadmin.site.register(Sale_Detail,Sale_DetailAdmin)
