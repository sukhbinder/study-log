from django.db import models
from django.utils import timezone

from django.urls import reverse

def days_hence(days=3):
    return timezone.now() + timezone.timedelta(days=days)

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class StudyLog(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    user = models.CharField(max_length=40)
    date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=300)
    next_review_date = models.DateTimeField(default=days_hence)
    
    
    def __str__(self):
        return "{} {} {} {}".format(self.date, self.subject, self.description)
    
    def get_absolute_url(self):
        return reverse('update-view', args=[str(self.id)])

    def get_user_url(self):
        return reverse('user-view', args=[str(self.user)])

