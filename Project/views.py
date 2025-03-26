from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import *
from django.http import HttpResponse
import io
from django.shortcuts import redirect

# Create your views here.
def renderPage(request):
    return render(request, "Project/index.html")


def insert(request):
    if request.method == "POST":
        
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        semester = request.POST.get('semester')
        profilePic = request.FILES.get('profilePic', None)

        # Create a dictionary from the POST data
        pythDic = {
            "name": name,
            "address": address,
            "contact": contact,
            "semester": semester,
            "profilePic": profilePic
        }

        serializeData = StudentDataSerializer(data=pythDic)
        if serializeData.is_valid():
            serializeData.save() 
            return redirect('showList') 
        else:
            error = JSONRenderer().render(serializeData.errors)
            return HttpResponse(error, content_type='application/json')
    
    return render(request, "Project/User.html")

def update(request, id):
    studentData = StudentData.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        semester = request.POST.get('semester')
        profilePic = request.FILES.get('profilePic', None)  # Correct way to handle file

        # Prepare dictionary for serializer (without profilePic)
        pythDic = {
            "name": name,
            "address": address,
            "contact": contact,
            "semester": semester,
        }

        # Serialize data without profilePic
        serializeData = StudentDataSerializer(studentData, data=pythDic, partial=True)
        if serializeData.is_valid():
            serializeData.save()

            # Only update profilePic if a new file is uploaded
            if profilePic:
                studentData.profilePic = profilePic
                studentData.save()

            return redirect('showList')
        else:
            error = JSONRenderer().render(serializeData.errors)
            return HttpResponse(error, content_type='application/json')

    return render(request, "Project/UpdateUser.html", {'student': studentData})


def allData(request):
    allData = StudentData.objects.all()
    serializedData = StudentDataSerializer(allData, many = True)
    return render(request, "Project/index.html", context={'data': serializedData.data})

def studentData(request, id):
    student_data = StudentData.objects.get(id = id)
    serializedData = StudentDataSerializer(student_data)
    jsonData = JSONRenderer().render(serializedData.data)
    return HttpResponse(jsonData, content_type='application/json')

def deleteStudent(request, id):
    student_delete = StudentData.objects.get(id=id)
    student_delete.delete()
    return redirect('showList')

def searchData(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip() 

        if not name:
            all_students = StudentData.objects.all()
        else:
            all_students = StudentData.objects.filter(name__icontains=name) 

        serializedData = StudentDataSerializer(all_students, many=True)  
        return render(request, "Project/index.html", context={'data': serializedData.data})
