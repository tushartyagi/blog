from django.contrib import admin
from post.models import Post

class PostAdmin(admin.ModelAdmin):
    fields = ('post_title', 'post_body',  'post_slug')
    readonly_fields = ('publish_date', 'edit_date')

admin.site.register(Post, PostAdmin)

