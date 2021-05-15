import datetime
from django.utils import timezone
from django.test import SimpleTestCase, TestCase
from django.core.urlresolvers import reverse, resolve
from mailer.views import IndexView
from mailer.models import Company, Contact, Order


class HomepageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)
    
    def test_homepge_template(self):
        self.assertTemplateUsed(self.response, 'mailer/index.html')
    
    def test_homepage_contains(self):
        self.assertContains(self.response, 'Mailer Info')
    
    def test_homepage_resolve(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, IndexView.as_view().__name__)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)


class CompanyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(
            name = 'Challenge Company',
            bic = '7889125-305'
        )
        
    def setUp(self):
        self.company.refresh_from_db()

    def test_company_record(self):
        self.assertEqual(self.company.name, 'Challenge Company')
        self.assertEqual(self.company.bic, '7889125-305')
        self.assertNotEqual(self.company.id, 400)

    def test_update_company_record(self):
        self.company.name = 'Metrix Ltd'
        self.company.bic ='6547033-672'
        self.assertNotEqual(self.company.name, 'Challenge Company')
        self.assertNotEquals(self.company.bic, '7889125-305')
        self.assertEqual(self.company.bic, '6547033-672')
        self.assertTrue(self.company.name, 'Metrix Ltd')


class OrderTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(
            name = 'Challenge Company',
            bic = '7889125-305'
        )
        
        cls.contact = Contact.objects.create(
            company = Company.objects.get(id=cls.company.id),
            full_name = 'Benjamin James Wilsom',
            email = 'contact@fruitvail.com'
        )

        cls.order = Order.objects.create(
            order_number = 'd9abc37e1d4846eebe803c783d0f1b0b',
            company = Company.objects.get(id=cls.company.id),
            contact = Contact.objects.get(company=cls.company.id),
            total = 1434.101279830,
            order_count_quantity = 4,
            order_date = datetime.datetime(2020, 11, 3).replace(tzinfo=timezone.utc)
        )

    def setUp(self):
        self.order.refresh_from_db()

    def test_order_record(self):
        self.assertEqual(self.order.order_number, 'd9abc37e1d4846eebe803c783d0f1b0b')
        self.assertEqual(self.order.company, self.order.company)
        self.assertTrue(self.order.order_date, timezone.now)
        self.assertNotEqual(self.order.id, 300)

    def test_update_order_record(self):
        self.order.order_number = 'trebjiu1d8gf5be803c783djki'
        self.order.total = '1434.6547033672'
        self.assertNotEqual(self.order.total, '1434.101279830')
        self.assertNotEquals(self.order.order_date, 
            datetime.datetime(2019, 11, 4).replace(tzinfo=timezone.utc))
        self.assertEqual(self.order.order_number, 'trebjiu1d8gf5be803c783djki')


class ContactTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(
            name = 'Challenge Company',
            bic = '7889125-305'
        )
        
        cls.contact = Contact.objects.create(
            company = Company.objects.get(id=cls.company.id),
            full_name = 'Benjamin James Wilsom',
            email = 'contact@fruitvail.com'
        )

    def setUp(self):
        self.contact.refresh_from_db()

    def test_contact_record(self):
        self.assertEqual(self.contact.company.name, self.company.name)
        self.assertEqual(self.contact.full_name, 'Benjamin James Wilsom')
        self.assertNotEqual(self.contact.email, 'changemail@orangefruitltd.com')

    def test_update_order_record(self):
        self.contact.full_name = 'Felix Camfield James'
        self.contact.email = 'changemail@orangefruitltd.com'
        self.assertNotEqual(self.contact.email, 'contact@fruitvail.com')
        self.assertNotEquals(self.contact.company, 'Movie Max Company' )
        self.assertEqual(self.contact.full_name, 'Felix Camfield James')
