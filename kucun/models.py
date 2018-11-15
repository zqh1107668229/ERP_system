from django.db import models
from datetime import datetime
from jinhuo.models import Dept,Supplier,Employee,Product,StoreHouse
# Create your models here.
#
# 进货合同
class BuyOrder(models.Model):
    buyOrder_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="进货合同编号")
    writedate = models.DateTimeField(default=datetime.now,verbose_name="合同签订日期")
    insuredate = models.DateTimeField(default=datetime.now,verbose_name="合同生效日期")
    enddate = models.DateTimeField(default=datetime.now,verbose_name="合同到期日期")
    dept = models.ForeignKey(Dept,verbose_name="签订部门",on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,verbose_name="供应商",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,verbose_name="合同主要负责人",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "进货合同表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.buyOrder_id



# 进货合同明细表
class BuyOrder_Detail(models.Model):
    buyOrder_id = models.ForeignKey(BuyOrder,verbose_name="进货合同编号",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,verbose_name="商品编号",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,verbose_name="商品数量")
    peice = models.IntegerField(default=0,verbose_name="商品进价(元)")
    class Meta:
        verbose_name = "进货合同表明细"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.buyOrder_id


# 入库单表
class EnterStock(models.Model):
    enterstock_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="入库单编号")
    enterdate = models.DateTimeField(default=datetime.now,verbose_name="入库时间")
    dept_id = models.ForeignKey(Dept,verbose_name="入库部门",on_delete=models.CASCADE)
    storehouse = models.ForeignKey(StoreHouse,verbose_name="所入仓库",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,verbose_name="入库负责人",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "入库单表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.enterstock_id

# 入库单明细
class EntersTock_Detail(models.Model):
    enterstock_id = models.ForeignKey(EnterStock,verbose_name="入库单编号",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,verbose_name="入库商品编号",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,verbose_name="商品数量")
    peice = models.IntegerField(default=0,verbose_name="商品进价(元)")
    class Meta:
        verbose_name = "入库单表明细"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.enterstock_id


# 退库单表
class BackStock(models.Model):
    backstock_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="退库单编号")
    enterdate = models.DateTimeField(default=datetime.now,verbose_name="退库时间")
    dept_id = models.ForeignKey(Dept,verbose_name="退库部门",on_delete=models.CASCADE)
    storehouse = models.ForeignKey(StoreHouse,verbose_name="所退仓库",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,verbose_name="退库负责人",on_delete=models.CASCADE)
    remark = models.CharField(max_length=100,null=True,blank=True, verbose_name="退库原因")
    class Meta:
        verbose_name = "退库单表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.backstock_id


# 退库单明细表
class BacksTock_Detail(models.Model):
    backstock_id = models.ForeignKey(BackStock,verbose_name="入库单编号",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,verbose_name="所退商品编号",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,verbose_name="退入数量")
    peice = models.IntegerField(default=0,verbose_name="商品价格(元)")
    class Meta:
        verbose_name = "退库单表明细"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.backstock_id

# 出库单表
class LeaveStock(models.Model):
    leavestock_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="出库单编号")
    enterdate = models.DateTimeField(default=datetime.now,verbose_name="出库时间")
    dept_id = models.ForeignKey(Dept,verbose_name="出库部门",on_delete=models.CASCADE)
    storehouse = models.ForeignKey(StoreHouse,verbose_name="所出仓库",on_delete=models.CASCADE)
    storehouse = models.ForeignKey(StoreHouse,verbose_name="所入仓库",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,verbose_name="退库负责人",on_delete=models.CASCADE)
    remark = models.CharField(max_length=100,null=True,blank=True, verbose_name="退库原因")
    class Meta:
        verbose_name = "出库单表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.leavestock_id

# 出库单明细表
class LeaveStock_Detail(models.Model):
    leavestock_id = models.ForeignKey(LeaveStock,verbose_name="入库单编号",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,verbose_name="所出商品编号",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,verbose_name="出库数量")
    peice = models.IntegerField(default=0,verbose_name="出库价格(元)")
    class Meta:
        verbose_name = "出库单表明细"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.leavestock_id

# 退货单表
class BackSale(models.Model):
    backsale_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="退货单编号")
    enterdate = models.DateTimeField(default=datetime.now,verbose_name="退货日期")
    dept_id = models.ForeignKey(Dept,verbose_name="退货部门",on_delete=models.CASCADE)
    storehouse = models.ForeignKey(StoreHouse,verbose_name="退入仓库",on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee,verbose_name="退货负责人",on_delete=models.CASCADE)
    remark = models.CharField(max_length=100,null=True,blank=True, verbose_name="退库原因")
    class Meta:
        verbose_name = "退货单表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.backsale_id

# 退货单明细表
class BackSale_Detail(models.Model):
    backsale_id = models.ForeignKey(LeaveStock,verbose_name="退货单编号",on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,verbose_name="所退商品编号",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0,verbose_name="退货数量")
    peice = models.IntegerField(default=0,verbose_name="价格(元)")
    class Meta:
        verbose_name = "退货单表明细"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.backsale_id

