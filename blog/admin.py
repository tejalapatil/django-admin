from django.contrib import admin
from . import models
# Register your models here.

class BlogAdminArea(admin.AdminSite):
    site_header = 'administration'


class TestAdminPermissions(admin.ModelAdmin):
    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.groups.filter(name='edtiors').exists():
            return True
        return True

    def has_view_permission(self, request, obj=None):
        return True

blog_site = BlogAdminArea(name='BlogAdmin')
blog_site.register(models.Post, TestAdminPermissions)
blog_site.register(models.Book)


