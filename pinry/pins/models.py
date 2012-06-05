from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.contrib.auth.models import User
#from thumbs import ImageWithThumbsField

import urllib2

YEARS = (
    (1990, "1990"),
    (1991, "1991"),
    (1992, "1992"),
    (1993, "1993"),
    (1994, "1994"),
    (1995, "1995"),
    (1996, "1996"),
    (1997, "1997"),
    (1998, "1998"),
    (1999, "1999"),
    (2000, "2000"),
    (2001, "2001"),
    (2002, "2002"),
    (2003, "2003"),
    (2004, "2004"),
    (2005, "2005"),
    (2006, "2006"),
    (2007, "2007"),
    (2008, "2008"),
    (2009, "2009"),
    (2010, "2010"),
    (2011, "2011"),
    (2012, "2012"),
)

class Movies(models.Model):
    name = models.TextField()
    year = models.IntegerField(blank=True, null=True ,max_length=2, choices=YEARS , default=2012) 
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='pins/pin') 
   
    def __unicode__(self):
        return self.name

class Pin(models.Model):
    movie = models.ForeignKey(Movies)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.movie.name

