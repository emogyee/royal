from django.shortcuts import render, redirect
from .models import ConsultationRequest,TeamMember,Testimonial
from django.core.mail import send_mail

# Create your views here.
def home(request):

    return render(request,'home.html')

def index(request):
    
    team_members = TeamMember.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_visible=True)
    
    context ={
        'team_members':team_members,
        'testimonials':testimonials
    }
    
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        organization_name = request.POST.get('organization_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')
        
        # Create a new ConsultationRequest object and save it to the database
        ConsultationRequest.objects.create(
            full_name=full_name,
            organization_name=organization_name,
            email=email,
            phone=phone,
            service=service,
            message=message,
        )

        # send to email
        send_mail(
            subject=f"New Consultation Request - {service}",
            message=f"""
            You have received a new consultation request from:
            Full Name: {full_name}
            Organization Name: {organization_name}
            Email: {email}
            Phone: {phone}
            Service: {service}
            Message: 
            {message}

            Submitted through the website.
            """,
            from_email="emogyee@gmail.com",
            recipient_list=["emogyee@gmail.com"],
            fail_silently=False
        )

        return redirect('index')  # Redirect to a success page or the same page after submission
      
    return render(request, 'index.html',context)

def about(request):
    return render(request,'about.html')