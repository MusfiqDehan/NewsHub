from django.contrib import admin
from .models import News

admin.site.site_header = "NewsHub Admin"
admin.site.site_title = "NewsHub Admin Area"
admin.site.index_title = "Welcome to NewsHub Admin"

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'headline', 'original_link', 'newspaper_name', 'img_link')


admin.site.register(News, NewsAdmin)
