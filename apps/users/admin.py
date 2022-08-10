from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('username',)
    list_display = ('id', 'username', 'email', 'phone')
    list_display_links = ('id', 'username',)
    search_fields = ('username__startswith',)
    list_per_page = 20
    save_on_top = True
    save_as = True

    class CustomUserAdmin(UserAdmin):
        def get_form(self, request, obj=None, change=False, **kwargs):
            form = super().get_form(request, obj, **kwargs)
            is_superuser = request.user.is_superuser
            disable_fields = set()

            if not is_superuser:
                disable_fields |= {
                    'username',
                    'is_superuser',
                }

            for f in disable_fields:
                if f in form.base_fields:
                    form.base_fields[f].disabled = True

            return form
