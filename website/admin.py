from django.contrib import admin

# Register your models here.
from .models import Nauczyciel


class NauczycielAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Nauczyciel, NauczycielAdmin)
