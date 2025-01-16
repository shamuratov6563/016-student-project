from django.contrib import admin
from .models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number')
    list_display_links = ('id',)
    search_fields = ('phone_number',)
    list_filter = ('is_staff',)
    list_editable = ('phone_number',)
    list_per_page = 100

    