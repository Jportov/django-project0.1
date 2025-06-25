from django.contrib import admin
from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    




class CarAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "factory_year", "model_year", "value")
    search_fields = ("model", "brand")
    
admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)

