from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Ticket, Worker, Notification
from .forms import TicketForm
from django.core.mail import send_mail
from django.conf import settings
from .utils import send_ticket_notification  # Import your email function




# Create your views here.

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()  # Save the ticket to the database
            send_ticket_notification(ticket)  # Send the email notification
            # Create a new notification
            message = f"A new ticket has been created for {ticket.worker.name}: {ticket.issue}"
            Notification.objects.create(ticket=ticket, message=message)
            return redirect('ticket_list')  # Redirect to the ticket list or another page
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})

def notification_center(request):
    notifications = Notification.objects.filter(read=False).order_by('-created_at')
    return render(request, 'tickets/notification_center.html', {'notifications': notifications})

# View to return the number of tickets as JSON data
def get_ticket_count(request):
    try:
        latest_ticket = Ticket.objects.latest('created_at')  # Get the latest ticket based on creation date
        latest_ticket_id = latest_ticket.id
    except Ticket.DoesNotExist:
        # If no tickets exist, set the latest ticket ID to zero
        latest_ticket_id = 0

    return JsonResponse({'latest_ticket_id': latest_ticket_id})
    return JsonResponse({'latest_ticket_id': latest_ticket.id})

def mark_as_read(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.read = True
    notification.save()
    return redirect('notification_center')

def home(request):
    return render(request, 'tickets/home.html')

def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_success')
    else:
        form = TicketForm()
    
    return render(request, 'tickets/ticket_form.html', {'form': form})

def ticket_success(request):
    return render(request, 'tickets/ticket_success.html')

def ticket_list(request):
    tickets = Ticket.objects.all()
    notifications = Notification.objects.filter(read=False)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets, 'notifications': notifications})

def send_ticket_notification(ticket):
    subject = f'Ticket Created: {ticket.issue}'
    message = f'The ticket with issue "{ticket.issue}" has been created.\nStatus: {ticket.status}\nCreated At: {ticket.created_at}'
    recipient_list = ['ibi.balami@gmail.com']  # Add the recipient email here

    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)