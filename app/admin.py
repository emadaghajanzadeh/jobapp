from django.contrib import admin
from app.models import JobPost

class jobAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "salary")
    list_filter = ('date', 'salary')
    search_fields = ("title", "description")
    # fields = ("title", ("description", "salary"))

    # To specify sections:
    fieldsets = (
        ('Basic Information', {
         'fields': ('title', 'description')
         }),
        ('More Information', {
         'classes': ('collapse', 'wide'),
         'fields': (('expiry', 'salary'), 'slug')
         }), 
    )
# Register your models here.
admin.site.register(JobPost, jobAdmin)
