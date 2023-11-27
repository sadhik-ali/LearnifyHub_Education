from django.shortcuts import render, get_object_or_404
from .models import Popular_Courses, Top_Subjects,Events,Testimonial
# from .models import Course
from django.http import HttpResponse
from .forms import ContactForm, CourseEnquiry, EventRegister
import json

# Create your views here.



def index(request):
    popular_courses = Popular_Courses.objects.all()
    top_subjects = Top_Subjects.objects.all()
    events = Events.objects.all()
    testimonial = Testimonial.objects.all()

    context = {
        'popular_courses': popular_courses,
        'top_subjects': top_subjects,
        'events': events,
        'testimonial': testimonial
    }
    
    return render(request, 'web/index.html', context)


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, 'web/contact.html', context)


def course(request):
    popular_courses = Popular_Courses.objects.all()
    context = {
        'popular_courses': popular_courses,
    }

    return render(request,'web/course.html',context)

def course_detail(request , slug):
    course = get_object_or_404(Popular_Courses, slug=slug)
    context = {
        "course" : course
    } 
    return render(request, 'web/course_detail.html', context)


def register(request):
    form = CourseEnquiry(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_register": True,
            "form": form,
        }
    return render(request, 'web/register.html',context)


def event_register(request):
    form = EventRegister(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }

    return render(request, 'web/event_register.html',context)


def about(request):
    return render(request, 'web/about.html')

