from django.contrib import admin

# Register your models here.
from .models import Bookmark
from .models import Tag


class BookmarkAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if request.user.id is not None:
            obj.user_cre = request.user
        obj.user_upd = request.user
        super().save_model(request, obj, form, change)


class TagAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if request.user.id is not None:
            obj.user_cre = request.user
        obj.user_upd = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag, TagAdmin)
