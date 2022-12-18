from django.db import models


# It will store W and M in the database and weekly and monthly are shown to the user.
NEWSLETTER_OPTION = [
    ('W', 'Weekly'),
    ('M', 'Monthly')
]
# Create your models here.

class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION, default='M')
