from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)