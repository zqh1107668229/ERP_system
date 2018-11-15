from django.db import models
from datetime import datetime
# Create your models here.

# 供应商表
class Supplier(models.Model):
    supplier_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="供应商编号")
    name = models.CharField(max_length=30, verbose_name="供应商名称")
    address = models.CharField(max_length=30, verbose_name="地址")
    phone = models.IntegerField(default=0,verbose_name="电话")
    postalcode = models.IntegerField(default=0,verbose_name="邮编")

    class Meta:
        verbose_name = "供应商表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.supplier_id+" "+self.name

# 部门表
class Dept(models.Model):
    dept_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="部门编号")
    name = models.CharField(max_length=30, verbose_name="部门名称")
    remark = models.CharField(max_length=50,null=True,blank=True, verbose_name="备注")
    class Meta:
        verbose_name = "部门表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.dept_id+" "+self.name

# 员工表
class Employee(models.Model):
    employee_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="员工编号")
    dept = models.ForeignKey(Dept,verbose_name="所属部门",on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name="姓名")
    gender = models.CharField(choices=(("male","男"),("female","女")),default="female",max_length=10)
    phone = models.IntegerField(default=0,verbose_name="电话")
    birthday = models.DateTimeField(default=datetime.now,verbose_name="出生日期")
    address = models.CharField(max_length=30, verbose_name="住址")
    IdentityCard = models.CharField(max_length=18, verbose_name="身份证")
    class Meta:
        verbose_name = "员工表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.employee_id+" "+self.name


# 仓库表
class StoreHouse(models.Model):
    storehouse_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="仓库编号")
    address = models.CharField(max_length=30, verbose_name="地址")
    phone = models.IntegerField(default=0,verbose_name="电话")
    employee = models.ForeignKey(Employee,verbose_name="操作员",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now,verbose_name="仓库成立日期")
    class Meta:
        verbose_name = "货物仓库表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.address



# 部门——供应商表
class Dept_Supplier(models.Model):
    dept_name = models.ForeignKey(Dept,verbose_name="部门名称",on_delete=models.CASCADE)
    supplier_name = models.ForeignKey(Supplier,verbose_name="供应商名称",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "部门——供应商表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.dept_name.name+"——"+self.supplier_name.name


# 商品规格表
class ProductSpec(models.Model):
    name = models.CharField(max_length=30, verbose_name="商品规格名称")
    employee = models.ForeignKey(Employee,verbose_name="操作员",on_delete=models.CASCADE)
    remark = models.CharField(max_length=50,null=True,blank=True, verbose_name="备注")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="创建时间")
    class Meta:
        verbose_name = "商品规格表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


# 商品计量单位表
class PriductUnit(models.Model):
    name = models.CharField(max_length=30, verbose_name="计量单位名称")
    employee = models.ForeignKey(Employee,verbose_name="操作员",on_delete=models.CASCADE)
    remark = models.CharField(max_length=50,null=True,blank=True, verbose_name="备注")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="创建时间")
    class Meta:
        verbose_name = "商品计量单位表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


# 商品目录表
class Product(models.Model):
    product_id = models.CharField(unique=True,default=0,max_length=20,verbose_name="商品编号")
    name = models.CharField(max_length=30, verbose_name="商品名称")
    productspec = models.ForeignKey(ProductSpec,verbose_name="商品规格",on_delete=models.CASCADE)
    priductunit = models.ForeignKey(PriductUnit,verbose_name="商品计量单位",on_delete=models.CASCADE)
    Price = models.IntegerField(default=0,verbose_name="参考价格(元)")
    employee = models.ForeignKey(Employee,verbose_name="操作员",on_delete=models.CASCADE)
    remark = models.CharField(max_length=50,null=True,blank=True, verbose_name="备注")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="创建时间")
    class Meta:
        verbose_name = "商品目录表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.product_id+" "+self.name

# 商品——供应商表
class Product_Supplier(models.Model):
    product = models.ForeignKey(Product,verbose_name="商品名称",on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,verbose_name="供应商名称",on_delete=models.CASCADE)
    class Meta:
        verbose_name = "商品——供应商表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.product.name+"——"+self.supplier.name



