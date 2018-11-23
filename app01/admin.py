from django.contrib import admin
from app01.models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ["title","time"] #查询条件
# 安装模型到Django自带的后台
admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)
admin.site.register(Classify)
admin.site.register(Picture)
admin.site.register(Comment)