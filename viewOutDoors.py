from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .AppFiles.LengualeOut import WorkFile
from .models import *


class OutDoorsPage(View):

    template_name = 'OutDoors.html'

    def get(self,request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:#filter
            information = []
            try:
                request.COOKIES['lenguage']
            except:
                request.session['Currentpage'] = 'outdoors'
                return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))
            return render(request, self.template_name, {
                'DataAll': Totalplanes.objects.filter(Razom_number__gte=100000),
                'lenguage': request.COOKIES['lenguage'],
                'SelectType' : TypePlanes.objects.all(),
                'SelectFormat': FormatPlanes.objects.all(),
                'SelectCity': CityPlanes.objects.all(),
                'SelectContactor': ContractorPlanes.objects.all(),
                'SelectSide': SidePlanes.objects.all(),
                'BaseObjLen': WorkFile.outLenguage("PageWorkRK"),
                'PanelLeft': WorkFile.outLenguage("OutDoorsPage"),
                'cordinate': {
                    "x": request.session.get('xCor', '49.806'),
                    "y": request.session.get('yCor', '31.399'),
                    "zoom": request.session.get('zoomCor', '7')
                    }
            })

    def post(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:
            allAgancy = Allagancy.objects.all()
            return render(request, self.template_name, {'Allagancy' : allAgancy})