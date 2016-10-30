from django.contrib import admin
# from .models import PurchaseOfLand
from django.utils.translation import ugettext_lazy as _

# class PurchaseOfLandAdmin(admin.ModelAdmin):
#     fieldsets = [
#             (_('General information'), {'fields': ['number', 'name', 'date']}),
#             (_('Active'), {'fields': ['active'], 'classes': ['collapse']}),
#         ]
#     readonly_fields = ('code',)
#     list_display = ('__str__', 'name')
#
#
# admin.site.register(PurchaseOfLand, PurchaseOfLandAdmin)