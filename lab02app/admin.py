from django.contrib import admin

# Register your models here.
from .models import Movie, Category, Cast 

class MovieAdmin(admin.ModelAdmin):
    list_filter = ("name",)
    search_fields = ("name",)
    list_display = ("name", "custom_col" )

    def custom_col(self, obj):
        return obj.name
    
    fieldsets = (
        ("First Set", {
            'fields': ('name', 'publication_date')
        }),
        
    )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category)
admin.site.register(Cast)
