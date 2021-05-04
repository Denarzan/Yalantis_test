from django.contrib import admin
from .models import Course


# Register our model in admin.
class Courses(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date', 'num_of_lectures')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('start_date', 'end_date')


admin.site.register(Course, Courses)