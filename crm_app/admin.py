from django.contrib import admin
from .models import User, Employee, Vacation

# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Vacation)
