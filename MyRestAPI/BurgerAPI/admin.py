from django.contrib import admin
from .models import Order,CustomerDetail,Ingredient

from .models import UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(CustomerDetail)
admin.site.register(Ingredient)