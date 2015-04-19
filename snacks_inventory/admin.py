# Register your models here.
from django.contrib import admin
from snacks_inventory.models import Snack, User, SnackConsumer


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User name', {'fields': ['user_name']}),
        ('User email', {'fields': ['user_email']}),
    ]
    list_display = ('user_name', 'user_email')
    list_filter = ['user_name', 'user_email']
    search_fields = ['user_name', 'user_email']

class SnackAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Item Name',               {'fields': ['name']}),
        ('Original Quantity', {'fields': ['original_quantity']}),
        ('User', {'fields': ['user']})
    ]
    list_display = ('name','original_quantity','user')
    list_filter = ['remaining_quantity', 'user']
    search_fields = ['name','user']


class SnackConsumersAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Snack Name', {'fields': ['consumed_snack_name']}),
        ('Consumed User', {'fields': ['consumed_user']}),
        ('Consumed Quantity', {'fields': ['consumed_quantity']}),
        ('Date consumed', {'fields': ['date_consumed']})
    ]
    list_display = ('consumed_snack_name', 'consumed_user', 'consumed_quantity', 'date_consumed')
    list_filter = ['consumed_snack_name', 'consumed_user', 'consumed_quantity', 'date_consumed']
    search_fields = ['consumed_snack_name', 'consumed_user']


admin.site.register(Snack, SnackAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(SnackConsumer, SnackConsumersAdmin)

