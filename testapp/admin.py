from django.contrib import admin

# Register your models here.
from testapp.models import Candidate,Advisor

admin.site.register(Candidate)
admin.site.register(Advisor)
