from django.db import models

# Create your models here.
class AdminOD(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects= models.Manager()

class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    addres=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class Students(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    profile=models.FileField()
    addres=models.TextField()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    Attendance_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)


class attendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    Attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class LeaveReport(models.Model):
    id=models.AutoField(primary_key=True)
    studen_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_mesage=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

class LeaveReportStaff(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_mesage=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

class feedBackStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()

class feedBackStaffs(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class NotificationStudent(models.Model):
    id=models.AutoField(primary_key=True)
    studen_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class NotificationSaffs(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    Updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()
