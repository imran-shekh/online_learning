from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from .models import *

from django.contrib.auth.hashers import check_password, make_password


def home(request):
    
    course_dtls = Course_Details.objects.all()
    context = {
        'course_dtls' : course_dtls
    }
    
    return render(request, "index.html",context=context)


def contact(request):
    return render(request, "contact.html")


def sign_up(request):
    if request.method == 'POST':
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')

        sign_obj = Signup(
            first_name=f_name,
            last_name=l_name,
            email=email,
            password=make_password(password),
            age=age,
            mobile=mobile,
            gender=gender
        )

        sign_obj.save()

        return HttpResponse("Registration Sucessfulllllll")


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')

        try:
            email_id = Signup.objects.get (email=email)
            if email_id:
                if check_password(password, email_id.password):
                    request.session['name'] = email_id.first_name
                    request.session['email'] = email_id.first_name
                    return redirect('home')
                else:
                    return HttpResponse("wrong password")
        except:
            return HttpResponse("Email not found")

def logout(request):
    request.session.clear()
    return redirect('home')

def course(request, slug):
    fetch_dtls = Course_Details.objects.get(slug=slug)
    s_no = request.GET.get('serial_no')
    videos = None
    if s_no is None:
        s_no = 1
    try:
        videos = Videos.objects.get(video_belong=fetch_dtls, video_seq=s_no)
        if videos.is_preview is False:
            if request.session.get('name') is None:
                return redirect('home')
            else:
                user_id = Signup.objects.get(
                    email=request.session['email'])

    except:
        return redirect('home')

    return render(request, 'course.html', {'co_dtls': fetch_dtls, 'video': videos})

