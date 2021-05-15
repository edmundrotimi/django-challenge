#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
import random
import traceback
from uuid import uuid4

from django.core.management.base import BaseCommand, CommandError
from django.db.transaction import atomic
from django.utils.text import slugify
from django.utils.timezone import now

from mailer.models import Company, Contact, Order
from entries.entry import fruits, company_suffixes, company_post_suffixes, firstnames, lastnames

def generate_company_name():
    name = "%s %s" % (random.choice(fruits), random.choice(company_suffixes))
    if random.randint(0, 1000) < 500:
        name += " %s" % random.choice(company_post_suffixes)
    return name


class Command(BaseCommand):
    help='generate records in DB'

    @atomic
    def handle(self, *args, **options):
        companies = 500
        contacts = 10
        orders = 10
        
        self.stdout.write(self.style.WARNING('About to create records(companies, contacts, orders) in the database'))

        for idx in range(0, companies):
            try:
                company = Company()
                company.name = generate_company_name()
                self.stdout.write("company %d/%d: %s" % (idx + 1, companies, company.name))
                company.bic = "%s-%s" % (random.randint(1000000, 9999999),
                                        random.randint(100, 999))
                company.save()

                max_contacts = contacts + random.randint(1, 10)

                for cdx in range(contacts, max_contacts):
                    contact = Contact()
                    contact.first_name = random.choice(firstnames)
                    contact.last_name = random.choice(lastnames)
                    contact.company = company
                    contact.email = "x%d@%s.com" % (random.randint(1, 10000000), slugify(company.name))
                    contact.save()
                    max_orders = orders + random.randint(1, 10)
                    for odx in range(orders, max_orders):
                        past = random.randint(1, 700)
                        order = Order()
                        order.order_number = uuid4().hex
                        order.company = company
                        order.contact = contact
                        order.total = random.random() * random.randint(100, 10000)
                        order.order_count_quantity = random.randint(1, orders) 
                        order.order_date = now() - datetime.timedelta(days=-past)
                        order.save()
            except Exception as e:
                self.stderr.write(self.style.ERROR('Stoping record creation...'))
                raise CommandError('Error! Failed to generate record. \n %s (%s)' % (e,traceback.format_exc()))


        self.stdout.write('Records Successfully created')
            
