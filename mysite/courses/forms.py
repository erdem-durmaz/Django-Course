from django import forms
from .models import Course

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class CourseForm(forms.Form):
    course_name = forms.CharField(max_length=100)
    pub_date = forms.DateTimeField()


class AttendeeForm(forms.Form):
    courses = Course.objects.all()
    new_list = [(course.id,course.course_name) for course in courses]
    course = forms.ChoiceField(choices=new_list,required=False)
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=200)
    votes = forms.IntegerField()

