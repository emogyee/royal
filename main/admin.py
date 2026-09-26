from django.contrib import admin
from .models import ConsultationRequest,TeamMember,Testimonial



# Register your models here.
@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'organization_name', 'email', 'phone', 'service', 'created_at')
    search_fields = ('full_name', 'organization_name', 'email', 'phone', 'service')
    list_filter = ('service', 'created_at')
    ordering = ('-created_at',)
    
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'designation')
    list_filter = ('is_active',)
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession', 'order', 'is_visible')
    list_editable = ('order', 'is_visible')
    search_fields = ('client_name', 'profession')
    list_filter = ('is_visible',)