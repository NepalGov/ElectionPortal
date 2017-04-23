from django.db import models

# Create your models here.
from django.contrib.auth.models import User #To use User's name in author

class Zone(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=20)
    zone = models.ForeignKey(Zone)
    vdc = models.IntegerField()
    municipality = models.IntegerField()
    population = models.IntegerField()
    voters = models.IntegerField()

    def __str__(self):
        return self.name

class Politicaldiv(models.Model):
    name = models.CharField(max_length=20)
    zone = models.ForeignKey(Zone)
    district = models.ForeignKey(District)
    MUNICI_VDC = (
        ('1', 'Municipality'),
        ('2', 'Vdc'),
    )
    group = models.CharField(max_length=1, choices=MUNICI_VDC)

    def __str__(self):
        return self.name

class Party(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    about = models.TextField()
    established = models.DateField()
    slogan = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Candidate(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    party = models.ForeignKey(Party)
    zone = models.ForeignKey(Zone)
    district = models.ForeignKey(District)
    politicaldiv = models.ForeignKey(Politicaldiv)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    votes = models.CharField(max_length=10)
    VOTE_STATUS = (
        ('W','Won'),
        ('C','Still Counting'),
        ('L','Lose'),
    )
    status = models.CharField(max_length=1, choices=VOTE_STATUS)
    age = models.IntegerField()
    criminalcase = models.IntegerField()
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    about = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    auther = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    posted = models.DateField(auto_now=True)
    POST_LOC = (
        ('4','Defult'),
        ('1','Home 1'),
        ('2','Home 2'),
        ('3','Home 3'),
    )
    home = models.CharField(max_length=1, choices=POST_LOC, default='4')
    content = models.TextField()

    def __str__(self):
        return self.title

class Feedback(models.Model):
    whatyouweredoing = models.TextField()
    whathappened = models.TextField()

    def __str__ (self):
        return self.whathappened
