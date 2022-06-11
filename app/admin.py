from django.contrib import admin
from import_export.admin import ImportExportMixin
from import_export import resources
# Register your models here.
from . models import User,Bunka
admin.site.register(User)
admin.site.register(Bunka)
