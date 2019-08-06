from django.contrib import admin
from .models import Post, Product, Company
from reversion.admin import VersionAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import User
from .models import Student, StudentCourses, StudentSports

# Register your models here.

@admin.register(Post)
class PostAdmin(VersionAdmin):
    pass

admin.site.register(Product)

@admin.register(Company)
class CompanyAdmin(VersionAdmin):
    pass

admin.site.unregister(Group)

@admin.register(Group)
class WebsimGroupAdmin(VersionAdmin, GroupAdmin):
    pass

class StudentCourseInline(admin.TabularInline):
    model = StudentCourses
    extra = 1


class StudentSportInline(admin.TabularInline):
    model = StudentSports
    extra = 1


class MyStudentAdmin(admin.ModelAdmin):
    inlines = (StudentCourseInline, StudentSportInline, )


@admin.register(Student)
class StudentAdmin(VersionAdmin, MyStudentAdmin):
    pass
