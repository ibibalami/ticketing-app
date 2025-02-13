from django.contrib import admin
from .models import Ticket

# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('worker', 'issue', 'created_at', 'status')  # Add 'status' here
    # Include 'status' in your form fields as needed