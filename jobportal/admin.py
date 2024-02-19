from django.contrib import admin

# importing the database tables
from . models import contact,PostJobs,employee
# Register your models here.
admin.site.register(contact)
admin.site.register(PostJobs)
admin.site.register(employee)
