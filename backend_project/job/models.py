from datetime import *
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.contrib.gis.db import models as gismodels
# from django.contrib.gis.geos import Point
from django.contrib.auth.models import User
import geocoder
import os

class JobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Intership = 'Intership'

class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'

class Industry(models.TextChoices):
    Business = 'Business' 'Business'
    IT = 'IT'
    Banking = 'Banking'
    Education = 'Education' 
    Telecomunications = 'Telecomunications'
    Others = 'Others'

class Experience(models.TextChoices):
    NO_EXPERIENCE = 'NO_EXPERIENCE'
    ONE_YEAR = 'ONE_YEAR'
    TWO_YEAR = 'TWO_YEAR'
    THREE_YEAR_PLUS = 'THREE_YEAR_PLUS'

def return_Date_time():
    now = datetime.now()
    return now + timedelta(days=10)

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    jobType = models.CharField(
        max_length=10,
        choices=JobType.choices,
        default=JobType.Permanent
        )
    education = models.CharField(
        max_length=10,
        choices=Education.choices,
        default=Education.Bachelors
        )
    industry = models.CharField(
        max_length=30,
        choices=Industry.choices,
        default=Industry.Business
        )
    experience = models.CharField(
        max_length=30,
        choices=Experience.choices,
        default=Experience.NO_EXPERIENCE
        )
    salary = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000000000)])
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point_lat = models.FloatField(null=True, blank=True)
    point_long = models.FloatField(null=True, blank=True)
    lastDate = models.DateTimeField(default=return_Date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        key = os.environ.get('GEOCODER_API')
        g = geocoder.mapquest(self.address, key=key)
        lat = g.lat
        lng = g.lng
        print("************",lat)
        print("************",lng)
        self.point_lat = round(lat, 7)
        self.point_long = round(lng, 7)
        super(Job, self).save(*args, **kwargs)