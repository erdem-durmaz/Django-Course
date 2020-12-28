from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse,Http404, HttpResponseRedirect, request
from .models import Course, Attendee
from django.shortcuts import render
from django.urls import reverse
from .forms import AttendeeForm, ContactForm, CourseForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required



def index(request):
    course_list = Course.objects.order_by('pub_date')
    context = {
        'course_list': course_list,
    }
    return render(request,'courses/index.html',context)

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # print(course.attendee_set.all())
    return render(request,'courses/detail.html', context={'course': course }) 
    
def results(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'courses/results.html', {'course': course})

def vote(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    print(request.POST['choice'])
    selected_attendee = course.attendee_set.get(pk=request.POST['choice'])
    selected_attendee.votes +=1
    selected_attendee.save()
    return HttpResponseRedirect(reverse('courses:results', args=(course_id,)))

def get_name(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
    else:
        form = ContactForm()
    return render(request,'courses/name.html',{'form':form})

# MainPage

def get_courses(request):
    courses = Course.objects.all()
    form = CourseForm()
    
    # Create New Course
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = Course(course_name = form.cleaned_data['course_name'], pub_date = form.cleaned_data['pub_date'])
            new_course.save()
            
    return render (request,template_name='courses/courses.html', context={'courses': courses,'form':form})

# Edit Course
def show_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    form = CourseForm({'course_name': course.course_name, 'pub_date':course.pub_date})
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course.course_name = form.cleaned_data['course_name']
            course.pub_date = form.cleaned_data['pub_date']
            course.save()
    return render(request, template_name='courses/show-course.html', context={'course': course, 'form':form})

#Create Attendee
def create_attendee(request):
    form2 = AttendeeForm()
    if request.method == 'POST':
        form2 = AttendeeForm(request.POST)
        # print(request.POST)

        if form2.is_valid():
            new_attendee = Attendee(
                course = Course.objects.get(pk=int(form2.cleaned_data['course'])),
                name = form2.cleaned_data['name'],
                email = form2.cleaned_data['email'],
                votes = int(form2.cleaned_data['votes'])
            )
            new_attendee.save()
    return render (request,template_name='courses/create-attendee.html',context={'form2':form2})

#Are You Sure?
def areyousure(request,course_id):
    course = get_object_or_404(Course,pk=course_id)
    return render (request, template_name='courses/areyousure.html',context={'course':course})


# Delete Course
def delete_course(request,course_id):
    course = get_object_or_404(Course,pk=course_id)
    course.delete()
    return HttpResponseRedirect(reverse('courses:courses'))

#Update Attendee
def update_attendee(request,attendee_id):
    attendee = get_object_or_404(Attendee,pk=attendee_id)
    
    form = AttendeeForm({
                'name' : attendee.name,
                'email' : attendee.email,
                'votes' : attendee.votes,
    })
    if request.method == 'POST':
        form = AttendeeForm(request.POST)
        if form.is_valid():
            attendee.course = Course.objects.get(pk=form.cleaned_data['course'])
            attendee.name = form.cleaned_data['name']
            attendee.email = form.cleaned_data['email']
            attendee.votes = form.cleaned_data['votes']
            attendee.save()
        return HttpResponseRedirect(reverse('courses:courses'))
    return render(request, template_name='courses/update-attendee.html', context={'attendee': attendee, 'form':form})


#Delete Attendee
def delete_attendee(request,attendee_id):
    attendee = get_object_or_404(Attendee,pk=attendee_id)
    attendee.delete()
    return HttpResponseRedirect(reverse('courses:courses'))