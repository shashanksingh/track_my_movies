from django.utils import simplejson
from django.http import HttpResponse , HttpResponseRedirect
from pinry.pins.models import Pin
from django.core.files import File
from django.core.files.images import ImageFile
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import redirect_to_login 
from django.contrib.auth.models import User
import urllib2
import hashlib
import imageHandler

def pins_recent(request, page=1):
    start_pin = abs(int(page) - 1) * 25
    end_pin = int(page) * 25

    pins = Pin.objects.order_by('-id')[start_pin:end_pin]
    recent_pins = []
    for pin in pins:
        recent_pins.append({
            'id': pin.id,
            'thumbnail': pin.Movie.thumbnail.url,
            'description': pin.Movie.description,
        })

    return HttpResponse(simplejson.dumps(recent_pins), mimetype="application/json")

def pins_add_form(request):
    mediaBM=str(request.GET.get('media'))
    return HttpResponse("<html><body onload=\"window.resizeTo(600,600)\"><p><img src=\""+mediaBM+"\"/><br/><form action=\"/api/pins/add\"><input type=\"hidden\" name=\"media\" value=\""+mediaBM+"\" /><h2 style=\"font: normal 18px 'Lobster', cursive , bold; \">Describe what you like?</h2><br/><input type=\"textarea\" value=\"Like\" name=\"description\"style=\"width:200px; height: 40px;\"/><br/><br/><input type=\"submit\" style=\"background-color:#DFDFDF; \"/></form></p></body></html>")

@login_required(login_url='/login_no_navbar/')
def pins_add(request):
    #current_url = resolve(request.get_full_path()).url_name
    mediaBM=str(request.GET.get('media'))
    #urlBM=str(request.GET.get('url'))
    descriptionBM=str(request.GET.get('description'))
    #titleBM=str(request.GET.get('title'))
    #is_videoBM=request.GET.get('is_video')
    nameHash = hashlib.sha224(mediaBM.split('/')[-1]).hexdigest()
    nameOfMedia = "pins/pin/" + nameHash + '.jpg'
    pinNew = Pin(url=mediaBM,description=descriptionBM,image=nameOfMedia,author=request.user)
    rawImage = imageHandler.downloadImage(mediaBM)
    imageHandler.saveImage(rawImage,nameHash)
    imageHandler.makeThumbnail(rawImage,nameHash)
    #imageHandler.makeThumbnail(nameHash)
    pinNew.save()
    return HttpResponse("<html><body onload=\"window.resizeTo(600,600)\"><p> <h2 style=\"font: normal 26px 'Lobster', cursive , bold;\" >Image Succesfully Loaded</h2><br/><img src=\""+mediaBM+"\"/><br/></p></body></html>")
