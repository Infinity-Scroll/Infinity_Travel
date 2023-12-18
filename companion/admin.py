from django.contrib import admin
from .models import Companion, Comment, Tag

admin.site.register(Companion)
admin.site.register(Comment)
admin.site.register(Tag)