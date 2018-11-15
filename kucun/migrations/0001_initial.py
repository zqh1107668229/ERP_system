# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-10 09:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jinhuo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backsale_id', models.CharField(default=0, max_length=20, unique=True, verbose_name='退货单编号')),
                ('enterdate', models.DateTimeField(default=datetime.datetime.now, verbose_name='退货日期')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='退库原因')),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Dept', verbose_name='退货部门')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Employee', verbose_name='退货负责人')),
                ('storehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.StoreHouse', verbose_name='退入仓库')),
            ],
            options={
                'verbose_name': '退货单表',
                'verbose_name_plural': '退货单表',
            },
        ),
        migrations.CreateModel(
            name='BackSale_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='退货数量')),
                ('peice', models.IntegerField(default=0, verbose_name='价格(元)')),
            ],
            options={
                'verbose_name': '退货单表明细',
                'verbose_name_plural': '退货单表明细',
            },
        ),
        migrations.CreateModel(
            name='BackStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backstock_id', models.CharField(default=0, max_length=20, unique=True, verbose_name='退库单编号')),
                ('enterdate', models.DateTimeField(default=datetime.datetime.now, verbose_name='退库时间')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='退库原因')),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Dept', verbose_name='退库部门')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Employee', verbose_name='退库负责人')),
                ('storehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.StoreHouse', verbose_name='所退仓库')),
            ],
            options={
                'verbose_name': '退库单表',
                'verbose_name_plural': '退库单表',
            },
        ),
        migrations.CreateModel(
            name='BacksTock_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='退入数量')),
                ('peice', models.IntegerField(default=0, verbose_name='商品价格(元)')),
                ('backstock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kucun.BackStock', verbose_name='入库单编号')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Product', verbose_name='所退商品编号')),
            ],
            options={
                'verbose_name': '退库单表明细',
                'verbose_name_plural': '退库单表明细',
            },
        ),
        migrations.CreateModel(
            name='BuyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyOrder_id', models.CharField(default=0, max_length=20, unique=True, verbose_name='进货合同编号')),
                ('writedate', models.DateTimeField(default=datetime.datetime.now, verbose_name='合同签订日期')),
                ('insuredate', models.DateTimeField(default=datetime.datetime.now, verbose_name='合同生效日期')),
                ('enddate', models.DateTimeField(default=datetime.datetime.now, verbose_name='合同到期日期')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Dept', verbose_name='签订部门')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Employee', verbose_name='合同主要负责人')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Supplier', verbose_name='供应商')),
            ],
            options={
                'verbose_name': '进货合同表',
                'verbose_name_plural': '进货合同表',
            },
        ),
        migrations.CreateModel(
            name='BuyOrder_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='商品数量')),
                ('peice', models.IntegerField(default=0, verbose_name='商品进价(元)')),
                ('buyOrder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kucun.BuyOrder', verbose_name='进货合同编号')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Product', verbose_name='商品编号')),
            ],
            options={
                'verbose_name': '进货合同表明细',
                'verbose_name_plural': '进货合同表明细',
            },
        ),
        migrations.CreateModel(
            name='EnterStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enterstock_id', models.CharField(default=0, max_length=20, unique=True, verbose_name='入库单编号')),
                ('enterdate', models.DateTimeField(default=datetime.datetime.now, verbose_name='入库时间')),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Dept', verbose_name='入库部门')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Employee', verbose_name='入库负责人')),
                ('storehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.StoreHouse', verbose_name='所入仓库')),
            ],
            options={
                'verbose_name': '入库单表',
                'verbose_name_plural': '入库单表',
            },
        ),
        migrations.CreateModel(
            name='EntersTock_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='商品数量')),
                ('peice', models.IntegerField(default=0, verbose_name='商品进价(元)')),
                ('enterstock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kucun.EnterStock', verbose_name='入库单编号')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Product', verbose_name='入库商品编号')),
            ],
            options={
                'verbose_name': '入库单表明细',
                'verbose_name_plural': '入库单表明细',
            },
        ),
        migrations.CreateModel(
            name='LeaveStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavestock_id', models.CharField(default=0, max_length=20, unique=True, verbose_name='出库单编号')),
                ('enterdate', models.DateTimeField(default=datetime.datetime.now, verbose_name='出库时间')),
                ('remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='退库原因')),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Dept', verbose_name='出库部门')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Employee', verbose_name='退库负责人')),
                ('storehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.StoreHouse', verbose_name='所入仓库')),
            ],
            options={
                'verbose_name': '出库单表',
                'verbose_name_plural': '出库单表',
            },
        ),
        migrations.CreateModel(
            name='LeaveStock_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='出库数量')),
                ('peice', models.IntegerField(default=0, verbose_name='出库价格(元)')),
                ('leavestock_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kucun.LeaveStock', verbose_name='入库单编号')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Product', verbose_name='所出商品编号')),
            ],
            options={
                'verbose_name': '出库单表明细',
                'verbose_name_plural': '出库单表明细',
            },
        ),
        migrations.AddField(
            model_name='backsale_detail',
            name='backsale_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kucun.LeaveStock', verbose_name='退货单编号'),
        ),
        migrations.AddField(
            model_name='backsale_detail',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jinhuo.Product', verbose_name='所退商品编号'),
        ),
    ]