from django.views.generic import ListView
from .models import Company, Contact, Order


class IndexView(ListView):
    model = Company
    template_name = "mailer/index.html"
    context_object_name= 'companies'
    paginate_by = 100

    def get_queryset(self):
        return Company.companyquery.group_by('name', 'bic', 'number_of_orders',
                                            'total_orders', 'total_paid', 'order_receipts')
    
    




 
