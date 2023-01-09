from django.contrib import admin

from apps.users.models import EmailVerification, User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username',)


class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    readonly_fields = ('created',)


admin.site.register(User, UserAdmin)
admin.site.register(EmailVerification, EmailVerificationAdmin)
