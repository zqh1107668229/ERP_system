from django.db import models
from datetime import datetime
from jinhuo.models import Dept,Supplier,Employee,Product
from kucun.models import BuyOrder
# Create your models here.


# 客户表
class Customer(models.Model):
    customer_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="客户编号")
    name = models.CharField(max_length=30, verbose_name="客户名称")
    address = models.CharField(max_length=30, verbose_name="地址")
    phone = models.IntegerField(default=0,verbose_name="电话")
    PostalCode = models.IntegerField(default=0,verbose_name="邮编")
    class Meta:
        verbose_name = "客户表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.customer_id+" "+self.name

# 销售合同
class SaleOrder(models.Model):
    saleorder_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="合同编号")
    writedate = models.DateTimeField(default=datetime.now,verbose_name="合同签订日期")
    insuredate = models.DateTimeField(default=datetime.now,verbose_name="合同生效日期")
    enddate = models.DateTimeField(default=datetime.now,verbose_name="合同到期日期")
    dept = models.ForeignKey(Dept,verbose_name="签订部门",on_delete=models.CASCADE)
    supplier = models.ForeignKey(Customer,verbose_name="客户编号",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,verbose_name="合同主要负责人",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "销售合同表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.saleorder_id

# 销售合同表明细
class SaleOrder_Detail(models.Model):
    saleorder_id = models.ForeignKey(SaleOrder,verbose_name="销售合同编号",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,verbose_name="销售商品编号",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,verbose_name="商品数量")
    peice = models.IntegerField(default=0,verbose_name="商品进价(元)")
    class Meta:
        verbose_name = "销售合同表明细"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.saleorder_id

# 进货表
class Buy(models.Model):
    buy_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="进货编号")
    comedate = models.DateTimeField(default=datetime.now,verbose_name="进货日期")
    dept = models.ForeignKey(Dept,verbose_name="进货部门",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,verbose_name="验货人",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "进货表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.buy_id

# 进货表明细
class Buy_Detail(models.Model):
    buy_id = models.ForeignKey(Buy,verbose_name="进货编号",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,verbose_name="商品编号",on_delete=models.CASCADE)
    buyorder_id = models.ForeignKey(BuyOrder,verbose_name="采购合同",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,verbose_name="商品数量")
    peice = models.IntegerField(default=0,verbose_name="商品进价(元)")
    class Meta:
        verbose_name = "进货表明细"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.buy_id

# 销售表
class Sale(models.Model):
    sale_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="销售编号")
    saledate = models.DateTimeField(default=datetime.now,verbose_name="销售日期")
    dept = models.ForeignKey(Dept,verbose_name="销售部门",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,verbose_name="售货人",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "销售表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.sale_id

# 销售明细
class Sale_Detail(models.Model):
    sale_id = models.ForeignKey(Sale,verbose_name="销售编号",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,verbose_name="商品编号",on_delete=models.CASCADE)
    buyorder_id = models.ForeignKey(SaleOrder,verbose_name="销售合同",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,verbose_name="商品数量")
    peice = models.IntegerField(default=0,verbose_name="商品进价(元)")
    discount = models.CharField(null=True,blank=True,max_length=20,verbose_name="折扣")
    class Meta:
        verbose_name = "销售表明细"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.sale_id