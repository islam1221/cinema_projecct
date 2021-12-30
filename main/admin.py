from django.contrib import admin
from .models import Cinema, Genres, Movie, Reviews

# Register your models here.
class ReviewInline(admin.StackedInline):
    model = Reviews
    extra = 1
class MovieAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    search_fields = ['title','description']
    list_display = 'id title cinema'.split()
    list_editable = 'cinema'.split()
    list_filter = 'genres cinema'.split()
admin.site.register(Cinema)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Genres)
admin.site.register(Reviews)