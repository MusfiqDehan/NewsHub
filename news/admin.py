from django.contrib import admin
from .models import News

admin.site.site_header = "NewsHub Admin"
admin.site.site_title = "NewsHub Admin Area"
admin.site.index_title = "Welcome to NewsHub Admin"

admin.site.register(News)
