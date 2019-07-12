from django.contrib import admin
from .models import Post, Product, Company
from reversion.admin import VersionAdmin
# Register your models here.

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(VersionAdmin):
    pass

admin.site.register(Product)

@admin.register(Company)
class CompanyAdmin(VersionAdmin):
    pass
