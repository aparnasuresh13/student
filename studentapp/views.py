from modulefinder import packagePathMap
from django.shortcuts import redirect,render
from studentapp.models import addstudent

# Create your views here.
def add_student(request):
    return render(request,'add.html')

def add_student_details(request):
    if request.method=='POST':
        sname=request.POST['student_name']
        email=request.POST['email']
        phno=request.POST['phone_number']
        adrs=request.POST['address']
        image=request.FILES.get('file')


        student=addstudent(student_name=sname,
                            email=email,
                            phone_number=phno,
                            address=adrs,image=image)
        
        print("Save data...")
        student.save()
        return redirect('show_details')


def show_details(request):
    students=addstudent.objects.all()
    return render(request,'showdetails.html',{'students':students})

def editpage(request,pk):
    students=addstudent.objects.get(id=pk)
    return render(request,'edit.html',{'students':students})

def edit_student_details(request,pk):
    if request.method=='POST':
        students=addstudent.objects.get(id=pk)
        students.student_name=request.POST.get('student_name')
        students.email=request.POST.get('email')
        students.phone_number=request.POST.get('phone_number')
        students.address=request.POST.get('address')
        students.image = request.FILES.get('file')
        students.save()
        return redirect('show_details')
    return render(request,'edit.html')

def deletepage(request,pk):
    students=addstudent.objects.get(id=pk)
    return render(request,'delete.html',{'students':students})

def delete_student(request,pk):
    students=addstudent.objects.get(id=pk)
    students.delete()
    return redirect('show_details')