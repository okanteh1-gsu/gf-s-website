from django.contrib import admin

# Register your models here.
from .models import HerInfo, RomanticImage

admin.site.register(HerInfo)
admin.site.register(RomanticImage)
