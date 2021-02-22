import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers 
from django.views.decorators.csrf import csrf_exempt
from estudianteapp.models import Subjects,SessionYearModel,Students,Subjects,Attendance,attendanceReport


def staff_home(request):
    return render(request,"staff_template/staff_home_template.html")

def staff_take_attendance(request):
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    sessions=SessionYearModel.objects.all()
    return render(request,"staff_template/staff_take_attendance.html",{"subjects":subjects,"sessions":sessions})

@csrf_exempt
def get_students(request):
    subject_id=request.POST.get("subject")
    session_years=request.POST.get("session_year")

    subject=Subjects.objects.get(id=subject_id)
    sesions_year = SessionYearModel.objects.get(id=session_years)
    students=Students.objects.filter(course_id=subject.course_id,sessionYearModel_id=sesions_year)
    list_data=[]

    for student in students:
        data_small={"id":student.admin.id,"name":student.admin.first_name+" "+ student.admin.last_name} 
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_attendance_data(request):
    student_ids=request.POST.get("student_ids")
    subject_id=request.POST.get("subject_id")
    attendance_date=request.POST.get("attendance_date")
    session_year_id=request.POST.get("session_year_id")

    subject_model=Subjects.objects.get(id=subject_id)
    session_model=SessionYearModel.objects.get(id=session_year_id)
    
    json_sstuden=json.loads(student_ids)

    try:
        attendance=Attendance(subject_id=subject_model,attendance_date=attendance_date,sessionYearModel_id=session_model)
        attendance.save()

        for stud in json_sstuden:
            student = Students.objects.get(admin=stud['id'])
            attendance_report=attendanceReport(student_id=student,attendance_id=attendance,status=stud['status'])
            attendance_report.save()
        #print(data[0]['id'])
        return HttpResponse("OK")
    except:
        return HttpResponse("ERR")

def staff_update_attendance(response):
    return render(request,"staff_template/staff_update_attendance.html")