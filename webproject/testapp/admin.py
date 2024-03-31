from django.contrib import admin

# Register your models here.
from testapp.models import RegModel
class RegAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','email','gender','password','rpassword']

admin.site.register(RegModel,RegAdmin)