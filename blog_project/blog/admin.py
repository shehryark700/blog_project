from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_at')
    list_filter = ('status', 'published_at', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    ordering = ('status', '-published_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('author__username', 'body')
    actions = ['approve_comments']

    @admin.action(description='Mark selected comments as approved')
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
