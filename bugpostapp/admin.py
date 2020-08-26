from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bugpostapp.models import MyUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Field Heading (extra credit)',
            {
                'fields': (
                    'age',
                    'displayname',
                    'homepage',
                )
            }
        )
    )


admin.site.register(MyUser, CustomUserAdmin)
