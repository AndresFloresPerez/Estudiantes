from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from estudianteapp.models import CustomUser,Staffs,Courses,Students,Subjects
from django.contrib import messages  
from django.core.files.storage import FileSystemStorage
from estudianteapp.form import AddStudentForm,EditStudent
from django.urls import reverse
 
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
            return HttpResponseRedirect(reverse("add_staff"))
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect(reverse("add_staff"))

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
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request,"Failed Added Course")
            return HttpResponseRedirect(reverse("add_course"))


def add_student(request):
    courses=Courses.objects.all()
    form=AddStudentForm()
    return render(request,"hod_template/add_student_template.html",{"courses":courses,"form":form})

def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddStudentForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            address=form.cleaned_data["address"]
            session_start=form.cleaned_data["session_start"]
            session_end=form.cleaned_data["session_end"]
            course_id=form.cleaned_data["courseid"]
            sex=form.cleaned_data["sex"]

            if request.FILES["profile"]:
                profile=request.FILES["profile"]
                fs=FileSystemStorage()
                filename=fs.save(profile.name,profile)
                profile_url=fs.url(filename)
            else:
                profile_url=None

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                user.students.address=address
                course_obj=Courses.objects.get(id=course_id)
                user.students.course_id=course_obj
                user.students.session_start_year=session_start
                user.students.session_end_year=session_end
                user.students.gender=sex
                if profile_url!=None:
                    user.students.profile=profile_url
                user.save()
                messages.success(request,"Successfully Added Staff")
                return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.error(request,"Failed to Add Staff")
                return HttpResponseRedirect(reverse("add_student"))
        else:
            form=AddStudentForm(request.POST)
            return render(request,"hod_template/add_student_template.html",{ "form":form})
 

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
            return HttpResponseRedirect(reverse("add_subject"))    
        except:
            messages.error(request,"Failed to Add Subject")
            return HttpResponseRedirect(reverse("add_subject"))


    
def manage_staff(request):
    staffs=Staffs.objects.all()
    return render(request,"hod_template/manage_staff_template.html",{"staffs":staffs})

def manage_student(request):
    students=Students.objects.all()
    return render(request,"hod_template/manage_student_template.html",{"students":students})

def manage_course(request):
    courses=Courses.objects.all()
    return render(request,"hod_template/manage_course_template.html",{"courses":courses})

def manage_subject(request):
    subjects=Subjects.objects.all()
    return render(request,"hod_template/manage_subject_template.html",{"subjects":subjects})

def edit_staff(request,staff_id ):
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,"hod_template/edit_staff_template.html",{"staff":staff,"id":staff_id})

def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        staff_id=request.POST.get("staff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        username=request.POST.get("username")
   


        try:
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()
            messages.success(request,"Successfully Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id} ))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id} ))


def edit_student(request,student_id):
    request.session["student_id"]=student_id
    student=Students.objects.get(admin=student_id)
    form=EditStudent()
    form.fields["email"].initial=student.admin.email
    form.fields["first_name"].initial=student.admin.first_name
    form.fields["last_name"].initial=student.admin.last_name
    form.fields["username"].initial=student.admin.username
    form.fields["address"].initial=student.address
    form.fields["courseid"].initial=student.course_id.id
    form.fields["sex"].initial=student.gender
    form.fields["session_start"].initial=student.session_start_year
    form.fields["session_end"].initial=student.session_end_year
    return render(request,"hod_template/edit_student_template.html",{"form":form,"id":student_id ,"username":student.admin.username})

def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        student_id=request.session["student_id"]
        if student_id==None:
            return HttpResponseRedirect("/manage_student/")

        form=EditStudent(request.POST,request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            email=form.cleaned_data["email"]
            address=form.cleaned_data["address"]
            username=form.cleaned_data["username"]
            session_start=form.cleaned_data["session_start"]
            session_end=form.cleaned_data["session_end"]
            course_id=form.cleaned_data["courseid"]
            sex=form.cleaned_data["sex"]

            if request.FILES.get("profile",False):
                profile=request.FILES["profile"]
                fs=FileSystemStorage()
                filename=fs.save(profile.name,profile)
                profile_url=fs.url(filename)
            else:
                profile_url=None
            try:
                user=CustomUser.objects.get(id=student_id)
                user.first_name=first_name
                user.last_name=last_name
                user.email=email
                user.username=username
                user.save()

                student_user=Students.objects.get(admin=student_id)
                student_user.address=address
                student_user.session_start_year=session_start
                student_user.session_end_year=session_end
                student_user.gender=sex
                course_obj=Courses.objects.get(id=course_id)
                student_user.course_id=course_obj
                if profile_url!=None:
                    student_user.profile=profile_url
                student_user.save()
                del request.session["student_id"]
                messages.success(request,"Successfully Edit Student")
                return HttpResponseRedirect(reverse("edit_student", kwargs={"student_id":student_id} ))
            except:
                messages.error(request,"Failed to Edit Student")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id} ))
        else:
            form=EditStudent(request.POST)
            student=Students.objects.get(admin=student_id)
            return render(request,"hod_template/edit_student_template.html",{"form":form,"id":student_id ,"username":student.admin.username})
 

def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"hod_template/edit_course_template.html",{"course":course,"id":course_id})


def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        course_name=request.POST.get("course_name")
        course_id=request.POST.get("course_id")

        try:
            course_update= Courses.objects.get(id=course_id)
            course_update.course_name=course_name
            course_update.save()
            messages.success(request,"Successfully Edit Student")
            return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id":course_id} ))
        except:
            messages.error(request,"Failed to Edit Student")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id} ))


def edit_subject(request,subject_id):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    subject=Subjects.objects.get(id=subject_id)
    return render(request,"hod_template/edit_subject_template.html",{"courses":courses,"staffs":staffs,"subject":subject,"id":subject_id})


def edit_subject_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        subject_name=request.POST.get("subject_name")
        subject_id=request.POST.get("subject_id")
        staff_id=request.POST.get("staffid")
        course_id=request.POST.get("courseid")

        try:
            
            subject_update= Subjects.objects.get(id=subject_id)
            subject_update.subject_name=subject_name
            staff=CustomUser.objects.get(id=staff_id)
            subject_update.staff_id=staff
            course= Courses.objects.get(id=course_id)
            subject_update.course_id=course
            subject_update.save()

            messages.success(request,"Successfully Edit Student")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id} ))
        except:
            messages.error(request,"Failed to Edit Student")
            return HttpResponseRedirect(reverse("edit_subject", kwargs={"subject_id":subject_id} ))
