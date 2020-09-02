from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from bugpostapp.models import MyUser


class Ticket(models.Model):
    objects = None
    N = 'N'
    IP = 'IP'
    Invalid = 'INV'
    D = 'D'
    status_choices = [
        (N, 'New'),
        (IP, 'In_Progress'),
        (D, 'Done'),
        (Invalid, 'Invalid'),
    ]
    title = models.CharField(max_length=50)
    filed_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    user_filed = models.ForeignKey(MyUser, related_name="user_filed", null=True, on_delete=models.CASCADE)
    ticket_status = models.CharField(
        max_length=3,
        choices=status_choices,
        default=N,
    )
    user_assigned = models.ForeignKey(MyUser, related_name="user_assigned", null=True, on_delete=models.CASCADE)
    user_completed = models.ForeignKey(MyUser, related_name="user_completed", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
