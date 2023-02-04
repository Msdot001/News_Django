from django.contrib import admin
from .models import Article, Comment 


class CommentInline(admin.TabularInline):     # another format is admin.StackedInline
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines =[
        CommentInline,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)

# Register your models here.
