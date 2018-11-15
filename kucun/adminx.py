import xadmin
from .models import BuyOrder,BuyOrder_Detail,EnterStock,EntersTock_Detail,BackStock,BacksTock_Detail,LeaveStock,LeaveStock_Detail,BackSale,BackSale_Detail


class BuyOrderAdmin(object):
    # 显示字段
    list_display = ['buyOrder_id','writedate','insuredate','enddate','dept','supplier','employee']
    # 搜索
    search_fields = ['buyOrder_id','writedate','insuredate','enddate','dept','supplier','employee']
    # 过滤器
    list_filter = ['buyOrder_id','writedate','insuredate','enddate','dept','supplier','employee']


class BuyOrder_DetailAdmin(object):
    # 显示字段
    list_display = ['buyOrder_id','product_id','quantity','peice']
    # 搜索
    search_fields = ['buyOrder_id','product_id','quantity','peice']
    # 过滤器
    list_filter = ['buyOrder_id','product_id','quantity','peice']


class EnterStockAdmin(object):
    # 显示字段
    list_display = ['enterstock_id','enterdate','dept_id','storehouse','employee']
    # 搜索
    search_fields = ['enterstock_id','enterdate','dept_id','storehouse','employee']
    # 过滤器
    list_filter = ['enterstock_id','enterdate','dept_id','storehouse','employee']


class EntersTock_DetailAdmin(object):
    # 显示字段
    list_display = ['enterstock_id','product_id','quantity','peice']
    # 搜索
    search_fields = ['enterstock_id','product_id','quantity','peice']
    # 过滤器
    list_filter = ['enterstock_id','product_id','quantity','peice']


class BackStockAdmin(object):
    # 显示字段
    list_display = ['backstock_id','enterdate','dept_id','storehouse','employee','remark']
    # 搜索
    search_fields = ['backstock_id','enterdate','dept_id','storehouse','employee','remark']
    # 过滤器
    list_filter = ['backstock_id','enterdate','dept_id','storehouse','employee','remark']


class BacksTock_DetailAdmin(object):
    # 显示字段
    list_display = ['backstock_id','product_id','quantity','peice']
    # 搜索
    search_fields = ['backstock_id','product_id','quantity','peice']
    # 过滤器
    list_filter = ['backstock_id','product_id','quantity','peice']


class LeaveStockAdmin(object):
    # 显示字段
    list_display = ['leavestock_id','enterdate','dept_id','storehouse','employee','remark']
    # 搜索
    search_fields = ['leavestock_id','enterdate','dept_id','storehouse','employee','remark']
    # 过滤器
    list_filter = ['leavestock_id','enterdate','dept_id','storehouse','employee','remark']


class Leavestock_DetailAdmin(object):
    # 显示字段
    list_display = ['leavestock_id','product_id','quantity','peice']
    # 搜索
    search_fields = ['leavestock_id','product_id','quantity','peice']
    # 过滤器
    list_filter = ['leavestock_id','product_id','quantity','peice']


class BackSaleAdmin(object):
    # 显示字段
    list_display = ['backsale_id','enterdate','dept_id','storehouse','employee','remark']
    # 搜索
    search_fields = ['backsale_id','enterdate','dept_id','storehouse','employee','remark']
    # 过滤器
    list_filter = ['backsale_id','enterdate','dept_id','storehouse','employee','remark']


class BackSale_DetailAdmin(object):
    # 显示字段
    list_display = ['backsale_id','product_id','quantity','peice']
    # 搜索
    search_fields = ['backsale_id','product_id','quantity','peice']
    # 过滤器
    list_filter = ['backsale_id','product_id','quantity','peice']


xadmin.site.register(BuyOrder,BuyOrderAdmin)
xadmin.site.register(BuyOrder_Detail,BuyOrder_DetailAdmin)
xadmin.site.register(EnterStock,EnterStockAdmin)
xadmin.site.register(EntersTock_Detail,EntersTock_DetailAdmin)
xadmin.site.register(BackStock,BackStockAdmin)
xadmin.site.register(BacksTock_Detail,BacksTock_DetailAdmin)
xadmin.site.register(LeaveStock,LeaveStockAdmin)
xadmin.site.register(LeaveStock_Detail,Leavestock_DetailAdmin)
xadmin.site.register(BackSale,BackSaleAdmin)
xadmin.site.register(BackSale_Detail,BackSale_DetailAdmin)


