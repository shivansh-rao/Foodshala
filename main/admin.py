from django.contrib import admin
from .models import fooditem
from .models import order
from .models import Profile

# Register your models here.
admin.site.site_header = "Foodshala Admin"
admin.site.site_title = "Foodshala Admin Portal"
admin.site.index_title = "Welcome to Foodshala"

admin.site.register(fooditem)
admin.site.register(order)
admin.site.register(Profile)
