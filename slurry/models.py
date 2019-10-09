from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('W','With Nicotine'),
    ('W/O','Without Nicotine'),
)

COUNTRY_CHOICES = (
    ('RU','RUSSIA'),
    ('US','USA'),
    ('CH','CHINA'),
    ('EN','ENGLAND'),
    ('FR','FRANCE'),
    ('GE','GERMANY'),
)

LANGUAGE_CHOICES = (
    ('RU','RUSSIA'),
    ('US','USA'),
    ('CH','CHINA'),
    ('EN','ENGLAND'),
    ('FR','FRANCE'),
    ('GE','GERMANY'),
)

STATUS_CHOICES = (
    ('RA','RECENTLY_ADDED'),
    ('MW','MOST_WATCHED'),
    ('TR','TOP_RATED'),
)

class Slurry(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='slurry')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=3)
    country=models.CharField(choices=COUNTRY_CHOICES,max_length=2)
    language = models.CharField(choices=COUNTRY_CHOICES, max_length=2)
    status=models.CharField(choices=STATUS_CHOICES, max_length=2)
