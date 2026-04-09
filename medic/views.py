from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Appointment, ContactMessage, Doctor

def index(request):
    return render(request, "index.html")

def appointment(request):
    departments = ["Cardiology", "Neurology", "Orthopedics"]
    doctors = ["Dr. John", "Dr. Sarah", "Dr. Michael"]

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        doctor = request.POST.get("doctor")
        date = request.POST.get("date")
        time = request.POST.get("time")

        # Save to DB
        Appointment.objects.create(
            name=name,
            email=email,
            department=department,
            doctor=doctor,
            date=date,
            time=time
        )
        print(f"Appointment created for {name}")

    return render(request, "appointment.html", {
        "departments": departments,
        "doctors": doctors
    })


def blog(request):
    return render(request, "blog.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        print(f"Message received from {name}")

    return render(request, "contact.html")

  


def testimonial(request):
    return render(request, "testimonial.html")

def team(request):
    doctors = [
        {
            "name": "Dr. John Doe",
            "specialization": "Cardiology Specialist",
            "description": "Expert in heart-related treatments with 10+ years experience.",
            "image": "img/team-1.jpg",
            "twitter": "#",
            "facebook": "#",
            "linkedin": "#",
        },
        {
            "name": "Dr. Sarah Smith",
            "specialization": "Neurology Specialist",
            "description": "Specialist in brain and nervous system disorders.",
            "image": "img/team-2.jpg",
            "twitter": "#",
            "facebook": "#",
            "linkedin": "#",
        },
        {
            "name": "Dr. Michael Brown",
            "specialization": "Orthopedic Specialist",
            "description": "Focused on bone and joint care.",
            "image": "img/team-3.jpg",
            "twitter": "#",
            "facebook": "#",
            "linkedin": "#",
        },
    ]

    return render(request, "team.html", {"doctors": doctors})


def service(request):
    return render(request, "service.html")

def search(request):
    doctors = [
        {
            "name": "Dr. John Smith",
            "specialization": "Cardiology Specialist",
            "description": "Dolor lorem eos dolor duo eirmod sea.",
            "image": "img/team-1.jpg"
        },
        {
            "name": "Dr. Sarah Lee",
            "specialization": "Neurology Specialist",
            "description": "Dolor lorem eos dolor duo eirmod sea.",
            "image": "img/team-2.jpg"
        },
        {
            "name": "Dr. Michael Brown",
            "specialization": "Orthopedic Specialist",
            "description": "Dolor lorem eos dolor duo eirmod sea.",
            "image": "img/team-3.jpg"
        }
    ]

    department = request.GET.get('department')
    keyword = request.GET.get('q')

    if department:
        doctors = [d for d in doctors if department.lower() in d['specialization'].lower()]
    
    if keyword:
        doctors = [d for d in doctors if keyword.lower() in d['name'].lower() or keyword.lower() in d['description'].lower()]

    return render(request, "search.html", {
        "doctors": doctors,
        "department": department,
        "keyword": keyword
    })



def price(request):
    return render(request, "price.html")

def details(request):
    return render(request, "detail.html")

def about(request):
    return render(request, "about.html")
