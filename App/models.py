from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Event(models.Model):
    STATUS_CHOICES = (('Wedding', 'Wedding'), ('Engagement', 'Engagement'),('Reception','Reception'),('Bachelor Party','Bachelor Party'),('Private Party','Private Party'),('Happy Birthday Party','Happy Birthday Party'),('Half Saree','Half Saree'),('Dhothi','Dhothi'),('Shashti Poorthi','Shashti Poorthi'));
    username = models.CharField(max_length=30 );
    EventName = models.CharField(max_length=30,choices=STATUS_CHOICES);
   # author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    Email = models.EmailField();
    EventDate = models.DateField();

    phone_number = models.CharField(max_length=12);
    #phonenumber=models.BigIntegerField()
    Alt_Phone_number = models.CharField(max_length=12,blank=True);
    Effordable_Amount = models.FloatField();
    Description = models.TextField()

def __str__(self):
  return self.username + self.EventName + self.Email + self.EventDate + self.phone_number + self.Effordable_Amount + self.Description ;
