from django.contrib import admin
from .models import Profile, AuthModel, Analytics

admin.site.register(Profile)
admin.site.register(AuthModel)
admin.site.register(Analytics)
