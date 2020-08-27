from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from bugpostapp.models import MyUser


class Ticket(models.Model):
    n = 'N'
    ip = 'IP'
    invalid = 'INV'
    d = 'D'
    status_choices = [
        (n, 'new'),
        (ip, 'in_progress'),
        (d, 'done'),
        (invalid, 'invalid'),
    ]
    title = models.CharField(max_length=50)
    filed_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    user_filed = models.ForeignKey(MyUser, related_name="user_filed", on_delete=models.CASCADE)
    ticket_status = models.CharField(
        max_length=3,
        choices=status_choices,
        default=n,
    )
    user_assigned = models.ForeignKey(MyUser, related_name="user_assigned", on_delete=models.CASCADE)
    user_completed = models.ForeignKey(MyUser, related_name="user_completed", on_delete=models.CASCADE)

    def __str__(self):
        return self.description
