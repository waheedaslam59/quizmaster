from django.contrib import admin
from .models import newsandupdate, StudentsToped, Comment, City, Blogs, Queries, Reviews, ProgramCategory,BooksCategory,FreeBooks,Programs, StudentLevel, Institutions, Admission
admin.site.register(newsandupdate)
admin.site.register(City)
admin.site.register(Institutions)
admin.site.register(StudentLevel)
admin.site.register(ProgramCategory)
admin.site.register(Programs)
admin.site.register(Admission)
admin.site.register(BooksCategory)
admin.site.register(FreeBooks)
admin.site.register(Blogs)
admin.site.register(Reviews)
admin.site.register(Queries)
admin.site.register(StudentsToped)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
# Register your models here.
