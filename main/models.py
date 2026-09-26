from django.db import models

# Create your models here.
class ConsultationRequest(models.Model):
    full_name = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField()
    service = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.full_name} - {self.service}"
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    
    #social media
    facebook_url = models.URLField(max_length=255, blank=True, null=True)
    x_url = models.URLField(max_length=255, blank=True, null=True)
    instagram_url = models.URLField(max_length=255, blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text='Order in which the team members appear on the site')
    
    class Meta:
        ordering = ['order','name']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
        
        
    def __str__(self):
        return self.name
    
    
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100) 
    profession = models.CharField(max_length=100) 
    feedback = models.TextField(max_length=100) 
    image = models.ImageField(upload_to='testimonials/')
    is_visible = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['order','-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
            
            
    def __str__(self):
        return self.client_name