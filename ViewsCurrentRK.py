from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .AppFiles.LengualeOut import WorkFile
from .models import *

class WorkCurrentRK(View):
    template_name = 'CurrentRK.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:  # filter
            try:
                request.session['SettingRKName']
            except:
                return HttpResponseRedirect(reverse_lazy('setting'))
            try:
                dataAll = RkCompany.objects.filter(rk=int(request.session['SettingRKName']))
                outCity = []
                for i in dataAll.values('Razom_number__city_standart').distinct():
                    outCity.append(CityPlanes.objects.get(id=i['Razom_number__city_standart']))
            except:
                outCity = None
                paramCity = None

            #print(WorkFile.outLenguage("PageWorkRK"))
            dataAll = RkCompany.objects.filter(rk=request.session['SettingRKName'])
            request.session['currentDataOut'] = list(dataAll.values())
            return render(request, self.template_name, {
                'Program' : RkCompany.objects.filter(rk= request.session['SettingRKName']),
                'NameRK' : Rk.objects.get(id=request.session['SettingRKName']),
                'BasicName': WorkFile.outLenguage("PageWorkRK"),
                'tableNameHead': WorkFile.outLenguage("tableHead"),
                'lenguage': request.COOKIES['lenguage'],
                'ForReach': outCity,
                'Reach': ReachCity.objects.filter(rk=int(request.session['SettingRKName']))
            })

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:
            try:
                request.session['SettingRKName']
            except:
                return HttpResponseRedirect(reverse_lazy('setting'))
            return render(request, self.template_name, {
                'Program': RkCompany.objects.filter(rk= request.session['SettingRKName']),
                'BasicName': WorkFile.outLenguage("PageWorkRK"),
                'tableNameHead': WorkFile.outLenguage("tableHead"),
                'NameRK': Rk.objects.get(id=request.session['SettingRKName']),
                'lenguage': request.COOKIES['lenguage'],
            })