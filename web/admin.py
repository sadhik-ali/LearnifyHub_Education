from django.contrib import admin

from .models import (Contact, CoursesEnquirys, Events, EventsRegister,
                     Popular_Courses, Testimonial, Top_Subjects)

# Register your models here.


@admin.register(Popular_Courses)
class Popular_CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)


admin.site.register(Top_Subjects)

admin.site.register(Events)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(CoursesEnquirys)
class CoursesEnquirysAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(EventsRegister)
class EventsRegisterAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher")
