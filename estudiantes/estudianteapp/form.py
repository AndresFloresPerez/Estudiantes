from django import forms
from estudianteapp.models import Courses,SessionYearModel


class DateInput(forms.DateInput):
    input_type="date"

class AddStudentForm(forms.Form):
    email=forms.CharField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="first_name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="last_name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    course_list=[]
    try:
        courses=Courses.objects.all()
        for course in courses:
            small_course=(course.id,course.course_name)
            course_list.append(small_course)

    except:
        course_list=[]

    sesion_list=[]
  
    sesions=SessionYearModel.objects.all()
    for sesion in sesions:
        small_ses=(sesion.id,str(sesion.session_start_year) +"   TO  "+ str(sesion.session_end_year))
        sesion_list.append(small_ses)

     


    courseid=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    gender_choice=(("Male","Male"),("Female","Female"))
    sex=forms.ChoiceField(label="sex",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id=forms.ChoiceField(label="Session Year",choices=sesion_list,widget=forms.Select(attrs={"class":"form-control"}))
    profile=forms.FileField(label="profile",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}))


class EditStudent(forms.Form):
    email=forms.CharField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="first_name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="last_name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    courses=Courses.objects.all()
    course_list=[]
    try:
        for course in courses:
            small_course=(course.id,course.course_name)
            course_list.append(small_course)
    except:
        course_list=[]

    sesion_list=[]
    try:
        sesions=SessionYearModel.objects.all()
        for sesion in sesions:
            small_ses=(sesion.id,str(sesion.session_start_year) +"  -   "+ str(sesion.session_end_year))
            sesion_list.append(small_ses)

    except:
        sesion_list=[]

    courseid=forms.ChoiceField(label="courseid",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    gender_choice=(("Male","Male"),("Female","Female"))
    sex=forms.ChoiceField(label="sex",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id=forms.ChoiceField(label="Session Year",choices=sesion_list,widget=forms.Select(attrs={"class":"form-control"}))
    profile=forms.FileField(label="profile",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)