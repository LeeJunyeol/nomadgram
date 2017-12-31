from django.contrib import admin
from . import models

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
  # pass: 이 클래스는 텅빈 클래스다.
  pass 

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
  pass

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
  pass
