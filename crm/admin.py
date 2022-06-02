from django.contrib import admin
from .models import order, StatusCrm, CommentCrm
# Register your models here.

admin.site.register(order)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)

