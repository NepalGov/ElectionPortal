from django.db import models

# Create your models here.
from django.contrib.auth.models import User #To use User's name in author

from markdownx.models import MarkdownxField #Mardwown
from django.core.urlresolvers import reverse #sitemaps return url

class Zone(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=20, unique=True)
    zone = models.ForeignKey(Zone)
    vdc = models.IntegerField(verbose_name="No. of VDC")
    municipality = models.IntegerField(verbose_name="No. of municipality")
    submetropolitan = models.IntegerField(verbose_name="No. of sub-metropolitan")
    metropolitan = models.IntegerField(verbose_name="No. of metropolitan")
    population = models.IntegerField(verbose_name="Total Population")
    voters = models.IntegerField(verbose_name="Total Voters")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Politicaldiv(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40, unique=True)
    zone = models.ForeignKey(Zone)
    district = models.ForeignKey(District)
    MUNICI_VDC = (
        ('1', 'Vdc'),
        ('2', 'Municipality'),
        ('3','Sub-Metropolitan'),
        ('4','Metropolitan'),
    )
    group = models.CharField(max_length=1, choices=MUNICI_VDC)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Party(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    about = MarkdownxField()
    established = models.DateField()
    slogan = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/logo')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self): #For Sitemap
        return reverse('partyprofile', kwargs={'slug': self.slug})


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
    POSITION = (
        ('1','Mayor'),
        ('2','Deputy Mayor'),
        ('3','Ward President'),
        ('4','Member'),
    )
    position = models.CharField(max_length=1, choices=POSITION, default='4')
    votes = models.CharField(max_length=10)
    VOTE_STATUS = (
        ('W','Won'),
        ('C','Still Counting'),
        ('L','Lose'),
    )
    status = models.CharField(max_length=1, choices=VOTE_STATUS)
    age = models.IntegerField()
    criminalcase = models.IntegerField(verbose_name="No. of Criminal cases")
    photo = models.ImageField(upload_to='images/photo', null=True, blank=True)
    about = MarkdownxField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Post(models.Model):
    auther = models.ForeignKey(User, verbose_name="Author")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    posted = models.DateField(auto_now=True)
    POST_LOC = (
        ('4','Defult'),
        ('1','Home 1'),
        ('2','Home 2'),
        ('3','Home 3'),
        ('5','Top Section'),
        ('6','Bottom Section'),
    )
    home = models.CharField(max_length=1, choices=POST_LOC, default='4',verbose_name="Choose Post Position")
    content = MarkdownxField()
    summary = models.CharField(max_length=300)

    def __str__(self):
        return self.title

    def get_absolute_url(self): #For Sitemap
        return reverse('post', kwargs={'slug': self.slug})


class Feedback(models.Model):
    whatyouweredoing = models.TextField(verbose_name="What you were doing")
    whathappened = models.TextField(verbose_name="What happened")

    def __str__ (self):
        return self.whathappened

class Country(models.Model):
    name = models.CharField(max_length=30)
    officialname = models.CharField(max_length=100, verbose_name="Official Name")
    population = models.IntegerField(verbose_name="Total Population")
    voters = models.IntegerField(verbose_name="Total Voters")
    mvoters = models.IntegerField(verbose_name="Total Male Voters")
    fvoters = models.IntegerField(verbose_name="Total Female Voters")
    tgvoters = models.IntegerField(verbose_name="Total Third Gender Voters")
    area = models.IntegerField(verbose_name="Total Area")
    parties = models.IntegerField(verbose_name="Total Registered Parties")

    def __str__ (self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    website = models.CharField(max_length=30)
    email = models.EmailField()
    about = MarkdownxField()

    def __str__ (self):
        return self.name

    class Meta:
        ordering = ['name']
