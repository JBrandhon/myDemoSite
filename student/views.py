from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render


def index(request):
    return HttpResponse(" please go to this page http://localhost:8000/student/login")

def detail(request, student_id, office_id):
    """return HttpResponse("You're looking at question %s." % question_id)"""
    return render(request, 'templates/student/detail.html' ,{ "student_id":student_id , "office_id":office_id  })

def login(request):
    return render(request, 'templates/student/login.html')

def office(request):
    idNumber=request.GET.get('idNumber')
    return render(request, 'templates/student/office.html', { 'idNumber' : idNumber } )

def transaction(request,student_id,office_id,transaction_id):
    return render(request, 'templates/student/transaction.html',{ "student_id":student_id , "office_id":office_id, "transaction_id":transaction_id  })

def send_sms(request,question_id):
    return render(request, 'templates/student/sendSMS.html')
