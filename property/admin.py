from django.contrib import admin

# Register your models here.
from .models import Property
from .models import Tag
from .models import Review

class PropertyAdmin(admin.ModelAdmin):
    list_display = ["user", "title", "city", "date_added"]
    class Meta:
        model = Property

class TagAdmin(admin.ModelAdmin):
    list_display = ["property", "tag"]
    class Meta:
        model = Tag

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["property", "user", "text"]
    class Meta:
        model = Review

admin.site.register(Property, PropertyAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Review, ReviewAdmin)
