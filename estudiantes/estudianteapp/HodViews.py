from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from estudianteapp.models import CustomUser,Staffs,Courses,Students,Subjects
from django.contrib import messages  
 
def admin_home(request):
    return render(request,"hod_template/home_template.html")

def add_staff(request):
    return render(request,"hod_template/add_staff_template.html")    


def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            user.staffs.address=address
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/add_staff")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/add_staff")

def add_course(request):
    return render(request,"hod_template/add_course_template.html")

def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        course_name=request.POST.get("course_name")
        try:
            course_model=Courses(course_name=course_name)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request,"Failed Added Course")
            return HttpResponseRedirect("/add_course")


def add_student(request):
    courses=Courses.objects.all()
    return render(request,"hod_template/add_student_template.html",{"courses":courses})

def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        session_start=request.POST.get("session_start")
        session_end=request.POST.get("session_end")
        course_id=request.POST.get("courseid")
        sex=request.POST.get("sex")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
            user.students.address=address
            course_obj=Courses.objects.get(id=course_id)
            user.students.course_id=course_obj
            user.students.session_start_year=session_start
            user.students.session_end_year=session_end
            user.students.gender=sex
            user.students.profile=""
            user.save()
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect("/add_student")

def add_subject(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_template/add_subject_template.html",{"courses":courses,"staffs":staffs})

def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        subject_name=request.POST.get("subject_name")
        staffid=request.POST.get("staffid")
        staff_obj=CustomUser.objects.get(id=staffid)
        course_id=request.POST.get("courseid")
        course_obj=Courses.objects.get(id=course_id)
        try:
            subject=Subjects.objects.create(subject_name=subject_name,course_id=course_obj,staff_id=staff_obj)
            subject.save()
            messages.success(request,"Successfully to Add Subject")
            return HttpResponseRedirect("/add_subject")    
        except:
            messages.error(request,"Failed to Add Subject")
            return HttpResponseRedirect("/add_subject")


    
def manage_staff(request):
    staffs=Staffs.objects.all()
    return render(request,"hod_template/manage_staff_template.html",{"staffs":staffs})

def manage_student(request):
    students=Students.objects.all()
    return render(request,"hod_template/manage_student_template.html",{"students":students})

def manage_course(request):
    courses=Courses.objects.all()
    return render(request,"hod_template/manage_course_template.html",{"courses":courses})