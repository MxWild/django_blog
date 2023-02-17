from django.contrib import admin

from blog.models import Post, Status, Tag


class StatusAdmin(admin.ModelAdmin):
    list_display = ('title',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)


admin.site.register(Status, StatusAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

