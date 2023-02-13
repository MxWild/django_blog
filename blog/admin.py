from django.contrib import admin

from blog.models import Post, Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)


admin.site.register(Post, PostAdmin)
admin.site.register(Status, StatusAdmin)
