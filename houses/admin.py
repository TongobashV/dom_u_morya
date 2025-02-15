from django.contrib import admin
from houses.models import House


# Register your models here.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "active"]
    list_filter = ["active"]