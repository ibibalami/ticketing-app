from django.db import models

# Create your models here.
# tickets/models.py

from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.department})"

class Ticket(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    issue = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('open', 'Open'), ('closed', 'Closed'), ('pending', 'Pending')], default='open')


    def __str__(self):
        return f"Ticket for {self.worker.name} - {self.created_at}"

class Notification(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.ticket.worker.name}: {self.message}"