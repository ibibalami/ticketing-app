# tickets/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_ticket_notification(ticket):
    subject = f'Ticket Created: {ticket.issue}'
    message = (
        f'The ticket with issue "{ticket.issue}" has been created.\n'
        f'Status: {ticket.status}\n'
        f'Created At: {ticket.created_at}'
    )
    recipient_list = ['ibi.balami@gmail.com']  # Add the recipient email here

    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
