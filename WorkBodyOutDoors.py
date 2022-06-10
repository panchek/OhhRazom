from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .AppFiles.LengualeOut import WorkFile
from .models import *
import traceback
from django.db.models import Max

class WorkBodyOutDoors(View):

    def post(self, request, flag, x, y, zoom):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:#filter
            information = []
            try:
                request.COOKIES['lenguage']
            except:
                request.session['Currentpage'] = 'outdoors'
                return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))
        if flag == "addMark":

            MaxRazom = Totalplanes.objects.aggregate(Max('Razom_number'))
            instAdress = AdressPlanes(
                adress_UA=request.POST.get('adress_UA'),
                adress_RU=request.POST.get('adress_RU'),
                adress_EN=request.POST.get('adress_EN')
            )
            instAdress.save()
            instLoc = LocationPlanes(
                Location_UA=" ",
                Location_RU=" ",
                Location_EN=" "
            )
            instLoc.save()
            Totalplanes(
                lat=request.POST.get('x'),
                lng=request.POST.get('y'),
                doors="н/д",
                Self_number=request.POST.get('self_numb'),
                Razom_number=int(MaxRazom['Razom_number__max']) + 1,
                type=TypePlanes.objects.get(id=int(request.POST.get('type'))),
                format=FormatPlanes.objects.get(id=int(request.POST.get('format'))),
                OTS="н/д",
                GRP="н/д",
                adress=instAdress,
                house=" ",
                city_standart=CityPlanes.objects.get(id=int(request.POST.get('city'))),
                side=SidePlanes.objects.get(id=request.POST.get('side')),
                loc=instLoc,
                Contractor=ContractorPlanes.objects.get(id=int(request.POST.get('Contactor'))),
                route=int(request.POST.get('route')) +90
            ).save()
            request.session["xCor"] = request.POST.get('x')
            request.session["yCor"] = request.POST.get('y')
            request.session["zoomCor"] = 15
            return HttpResponseRedirect(reverse_lazy('outdoors'))
        elif flag == "deleteMark":
            request.session["xCor"] = x
            request.session["yCor"] = y
            request.session["zoomCor"] = zoom
            instTotal = Totalplanes.objects.get(Razom_number=int(request.POST.get('numb')))
            instTotal.delete()
            return HttpResponseRedirect(reverse_lazy('outdoors'))
        elif flag == "addPhoto":
            instTotal = Totalplanes.objects.get(Razom_number=int(request.POST.get('numb')))
            try:
                request.FILES['userfilePhoto'].name = str(request.POST.get('numb')) + '.jpg'
                instTotal.imagePhoto = request.FILES['userfilePhoto']
            except:
                pass
            try:
                request.FILES['userfileShema'].name = str(request.POST.get('numb')) + '.jpg'
                print("No")
                instTotal.imageShema = request.FILES['userfileShema']
            except:
                pass
            instTotal.save()
            request.session["xCor"] = x
            request.session["yCor"] = y
            request.session["zoomCor"] = zoom
            return HttpResponseRedirect(reverse_lazy('outdoors'))
        else:
            raise Http404


class ChangeLenguageOut(View):

    def post(self, request):
        request.session['Currentpage'] = "outdoors"
        request.session['inLenluage'] = request.POST.get('Len')
        return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))