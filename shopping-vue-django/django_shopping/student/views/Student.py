from django.shortcuts import render,HttpResponse


from student.models import Student, Grade


def index(request):
    return HttpResponse('index')

def getgrade(request):
    student = Student.objects.get(pk=1)
    grade = student.s_grade
    return HttpResponse('grade is %s' % grade.g_name)


def getStudents(request):
    grade = Grade.objects.get(pk=1)
    students = grade.student_set.all()
    # students = Student.objects.filter(s_grade=2)
    student1 = Student.objects.filter(pk=2).first()
    student1.s_grade_id = 2
    student1.save()

    names = ''
    for s in students:
        names = names + '   ' + s.s_name
    return HttpResponse(names)


def student(request,s_id):
    return HttpResponse(s_id)


def get_date(request,year,month):
    y = year
    m = month
    return HttpResponse(m + ' ' + y)