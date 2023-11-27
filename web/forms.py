# web/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact, CoursesEnquirys, EventsRegister
from django.forms import widgets


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Name"}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Phone"}),
            "subject": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your subject"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
            "message": widgets.Textarea(attrs={"class": "required form-control","placeholder": "Type Your Message",}),
        }



class CourseEnquiry(forms.ModelForm):
    class Meta:
        model = CoursesEnquirys
        exclude = ("timestamep",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Name"}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Phone"}),
            "subject": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your subject"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
            "message": widgets.Textarea(attrs={"class": "required form-control","placeholder": "Type Your Message",}),
        }

class EventRegister(forms.ModelForm):
    class Meta:
        model = EventsRegister
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Name"}),
            "phone": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your Phone"}),
            "subject": widgets.TextInput(attrs={"class": "required form-control", "placeholder": "Your subject"}),
            "email": widgets.EmailInput(attrs={"class": "required form-control","placeholder": "Your Email Address",}),
            "message": widgets.Textarea(attrs={"class": "required form-control","placeholder": "Type Your Message",}),
        }


