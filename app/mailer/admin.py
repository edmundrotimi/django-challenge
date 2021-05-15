#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Company, Contact, Order


class ContactTab(admin.TabularInline):
    model= Contact

class OrderTab(admin.TabularInline):
    model= Order
    raw_id_fields=['company',]


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'bic']
    list_display_links = ['name', 'bic']
    search_fields = ['name', 'bic']
    readonly_fields = ['number_of_orders', 'total_orders', 'total_paid', 'order_receipts']
    list_per_page = 50
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = False
    inlines=[ContactTab,]


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'full_name']
    list_display_links = ['id', 'company', 'full_name']
    search_fields = ['id', 'company', 'full_name']
    list_per_page = 50
    #readonly_fields = ['email',]
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = False
    raw_id_fields = ['company',]
    inlines=[OrderTab,]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'company', 'contact', 
        'total', 'order_count', 'order_date','modified_date']
    list_display_links = ['order_number', 'company']
    search_fields = ['order_number', 'company__name']
    fields = ['order_number', 'company', 'contact', 'order_count',
        'total', 'order_date']
    list_per_page = 50
    raw_id_fields = ['company', 'contact']
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = False

    def order_date(self, obj):
        return obj.order_date
    order_date.empty_value_display = '***No Order Date Provided***'


admin.site.register(Company, CompanyAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Order, OrderAdmin)