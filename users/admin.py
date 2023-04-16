from django.contrib import admin

from users.models import StudentUser


@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name", "student_class", "division"]