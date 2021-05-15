import json
import decimal
from django.dispatch import receiver
from django.db import transaction
from django.db.models import F
from django.db.models.signals import post_save
from .models import Order, Company, Contact
from .receipt_duplicate_finder import update_string_field


@receiver(post_save, sender='mailer.Order')
def update_fields_before_saving(sender, instance, **kwargs):
    
    with transaction.atomic():

        #get instance
        previous_state = Company.objects.get(bic=instance.company.bic)
        
        #check if there isa previous record
        if previous_state:

            #get contact for order
            order_client_name = instance.contact

            #get contact for quantity ordered
            order_client_order_count = instance.order_count_quantity

            # merge contact fullname with the order count using dictionary
            order_receipt = f'{instance.contact.full_name} : {order_client_order_count}'
        
            # previous state of the order_receipts fo the company
            #making the sales
            previous_receipt_list = previous_state.order_receipts

            #call update order receipt function
            receipt_update = update_string_field(previous_state.order_receipts, 
                                                instance.contact.full_name, instance.order_count)
            
            receipt_update_receipt = receipt_update

            #update records by icrementing by ! for each
            #successful order
            number_of_orders = previous_state.number_of_orders +  1.0

            #get the total order of the company
            if instance.order_count_quantity:

                total_orders = instance.order_count_quantity + previous_state.total_orders
            else:

                total_orders = previous_state.total_orders

            #total amount paid
            total_paid = decimal.Decimal(instance.total) + previous_state.total_paid 

            # updated_receipt_list = previous_receipt_list + str(order_receipt)
            update_records = Company(number_of_orders=number_of_orders, 
                                        total_orders=total_orders, total_paid=total_paid, 
                                        order_receipts=receipt_update_receipt )

            #get the instace of update_records
            update_records.id = instance.company.id

            #save only the updated fields
            update_records.save(update_fields=['number_of_orders', 'total_orders', 
                                            'total_paid', 'order_receipts'])                
