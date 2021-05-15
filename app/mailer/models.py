#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db.models import QuerySet
from django.utils.encoding import python_2_unicode_compatible
from django_group_by import GroupByMixin


class OrderQuerySet(QuerySet, GroupByMixin):
    pass


class Company(models.Model):
    name = models.CharField(max_length=150) 
    bic = models.CharField(max_length=250, blank=True)
    #number_of_orders is the number of times orders were made
    number_of_orders = models.IntegerField(blank=True, null=True, default=0) 
    #total_orders is the total sum of all individual number_of_orders
    total_orders = models.IntegerField(blank=True, null=True, default=0) 
    #total_paid is the sum total paid for all orders 
    total_paid = models.DecimalField(max_digits=18, decimal_places=9, blank=True, 
                                    null=True, verbose_name='total', default=0.0)
    #order_receipts contains contacts and their respective number_of_orders
    order_receipts = models.TextField(max_length=5000, blank=True, null=True, default='')
    objects = models.Manager()
    companyquery = OrderQuerySet.as_manager() 

    def __str__(self):
        return '%s' %(self.name)

    class Meta:
        verbose_name_plural = 'Companies'


class Contact(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    company = models.ForeignKey(Company, related_name="contacts", 
                        on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.full_name}'

    def save(self, *args, **kwargs):
        self.full_name = f'{self.first_name} {self.last_name}'
        super().save(*args, **kwargs)


@python_2_unicode_compatible
class Order(models.Model):
    order_number = models.CharField(max_length=150)
    company = models.ForeignKey(Company, related_name="orders", on_delete=models.CASCADE) 
    contact = models.ForeignKey(Contact, related_name="orders", on_delete=models.CASCADE) 
    total = models.DecimalField(max_digits=18, decimal_places=9) 
    order_date = models.DateTimeField(null=True, blank=True)
    # for internal use only
    added_date = models.DateTimeField(auto_now_add=True)
    # for internal use only
    modified_date = models.DateTimeField(auto_now=True)
    #number of order
    order_count = models.IntegerField(default=1, blank=True, null=True)
    #total quantity ordered
    #order_count_quantity = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.order_number