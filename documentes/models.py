from django.db import models
import uuid
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from chart_account.models import ChartAccaunt
from django.contrib.auth.models import User
from registeres.models import Stock


class BaseDocumentes(models.Model):
    code = models.UUIDField( default=uuid.uuid4, verbose_name = _('Unique code'), editable=False)
    user = models.ForeignKey(User, verbose_name=_('User'))
    date = models.DateTimeField(default=datetime.now, verbose_name = _('Date creation'))
    active = models.BooleanField(verbose_name = _('Active'), default=True)
    name = models.CharField(max_length=255, verbose_name = _('Full name'))
    number = models.CharField(max_length=255, verbose_name = _('Number'))
    chart_account_active = models.ManyToManyField(ChartAccaunt, verbose_name = _('Chart Accaunt Active'),
                            related_name='%(class)s_related_active', null=True)
    chart_account_passive = models.ManyToManyField(ChartAccaunt, verbose_name=_('Chart Accaunt Passive'),
                            related_name='%(class)s_related_passive', null=True)

    class Meta:
        abstract = True

        app_label = 'PurchaseInvoiceDocument'



#приходна накладна
class PurchaseInvoiceDocument(BaseDocumentes):
    stock_register = models.ForeignKey(Stock, verbose_name=_('Stock Register'))




#Купівля землі
# class PurchaseOfLand(BaseDocumentes):
#     #number = None
#     prefix_doc = models.CharField(default=_('POL'), max_length=22)
#
#
#     def save(self):
#         self.number = '%s  %s' %(self.prefix_doc, self.pk)