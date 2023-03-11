from django.contrib import admin


from .models import (
    Material,
    Assignment,
)

# Register your models here.

admin.site.register(Material)
admin.site.register(Assignment)