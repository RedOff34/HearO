from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user_id', 'name', 'email', 'phone_num', 'emergency', 'address', 'gender', 'birth', 'is_admin','medical_info' )
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Personal info', {'fields': ('name', 'email', 'phone_num', 'emergency', 'address', 'gender', 'birth','medical_info')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
 
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'password1', 'password2', 'name', 'email', 'phone_num', 'emergency', 'address', 'gender', 'birth','medical_info')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
