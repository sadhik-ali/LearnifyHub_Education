from django.contrib import admin
from . models import Popular_Courses,Top_Subjects,Events,Contact,CoursesEnquirys,EventsRegister,Testimonial
# Register your models here.


@admin.register(Popular_Courses)
class Popular_CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
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