from django.contrib import admin
from courts.models import Court


class CourtAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Court Name',               {'fields': ['name']}),
        ('Latitude',               {'fields': ['latitude']}),
        ('Longitude',               {'fields': ['longitude']}),
        ('Locality',               {'fields': ['locality']}),
        ('City',               {'fields': ['city']}),
        ('Court Type',               {'fields': ['court_type']}),
        ('Shoes Type Allowed',               {'fields': ['shoes_type_allowed']}),
        ('Open Court Type',               {'fields': ['open_court_type']})
    ]
    list_display = ('name','city','locality','court_type','shoes_type_allowed','open_court_type')
    list_filter = ['name','city','locality','court_type','shoes_type_allowed','open_court_type']
    search_fields = ['name','city','locality']


admin.site.register(Court, CourtAdmin)
