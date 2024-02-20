from django.contrib import admin
from .models import OAuthClient, AccessToken, RefreshToken

# Optionally, you can create custom admin classes to customize the admin interface
class OAuthClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'client_id', 'user')
    search_fields = ('name', 'client_id')

class AccessTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'client', 'expires')
    search_fields = ('token',)

class RefreshTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'access_token', 'expires')
    search_fields = ('token',)

# Register your models here
admin.site.register(OAuthClient, OAuthClientAdmin)
admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(RefreshToken, RefreshTokenAdmin)
