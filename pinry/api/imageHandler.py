import urllib2
import hashlib
import os, sys
import Image
from django.core.files.images import ImageFile
from django.conf import settings

MAX_THUMBNAIL_SIZE = 200 , 1000

def saveImage(tempImage,nameOfMedia):
   """saves the raw content of files"""
   fOrig = open(settings.MEDIA_DIR+nameOfMedia+".jpg",'w')
   imgTemp = ImageFile(fOrig)
   imgTemp.write(tempImage)
   imgTemp.flush()
   imgTemp.close()

#FIXME : PIL is thorwing  decoder jpeg not available
#def makeThumbnail(nameOfMedia):
def makeThumbnail(tempImage,nameOfMedia):
   """makes thumbnails of max size 200x1000 from raw content and save it"""
   #imgTemp = Image.open("/opt/sources/code/pinry/media/pins/pin/"+nameOfMedia+".jpg")
   #imgTemp.thumbnail(MAX_THUMBNAIL_SIZE , Image.ANTIALIAS )
   #imgTemp.save("/opt/sources/code/pinry/media/pins/pin/"+nameOfMedia+".200x1000.jpg", "JPEG")
   fThumb = open(settings.MEDIA_DIR+nameOfMedia+".200x1000.jpg",'w')
   imgTemp = ImageFile(fThumb)
   imgTemp.write(tempImage)
   imgTemp.flush()
   imgTemp.close()

def downloadImage(url):
   """download raw contents of a url """
   return urllib2.urlopen(url).read()
   

def calculateHash(text):
   """calcuate hash , its here for standardization """
   return hashlib.sha224(text).hexdigest()
