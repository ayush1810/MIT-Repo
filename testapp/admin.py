from django.contrib import admin
from testapp.models import Semester,Branch,Subject
# Register your models here.
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(Branch)
