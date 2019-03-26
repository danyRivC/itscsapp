from django.contrib import admin
from itscsapp.comment.models.comment import Comment


@admin.register(Comment)
class CommentCarrerAdmin(admin.ModelAdmin):
    list_display = ['author']
    readonly_fields = ['created', 'updated']
