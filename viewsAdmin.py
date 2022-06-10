import traceback

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views import View

from .AppFiles.LengualeOut import WorkFile
from .AppFiles.OutColorFile import WorkFiels
from django.urls import reverse_lazy
from .models import *
#from django.db.models import Q


class Admin(View):
    template_name = 'FinalyAdmin.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                request.COOKIES['lenguage']
            except:
                request.session['Currentpage'] = 'Admin'
                return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))
            try:
                dataAll = RkCompany.objects.filter(rk=int(request.session['currentOutAC']))
                try:
                    if request.session['advancedSearchType'] == "doors":
                        dataAll = dataAll.filter(Razom_number__doors__in = request.session['advancedSearchCodes'])
                    elif request.session['advancedSearchType'] == "Self_number":
                        dataAll = dataAll.filter(Razom_number__Self_number__in=request.session['advancedSearchCodes'])
                    elif request.session['advancedSearchType'] == "Razom_number":
                        dataAll = dataAll.filter(Razom_number__Razom_number__in=request.session['advancedSearchCodes'])
                except Exception as e:
                    print(traceback.format_exc())
                try:
                    dataAll = dataAll.filter(Razom_number__city_standart__id__in = request.session['filterCity'])
                    paramCity = CityPlanes.objects.filter(id__in=request.session['filterCity'])
                except:
                    paramCity = None

                try:
                    dataAll = dataAll.filter(Razom_number__type__id__in = request.session['filterType'])
                    paramType = FormatPlanes.objects.filter(id__in=request.session['filterType'])
                except:
                    paramType = None

                try:
                    dataAll = dataAll.filter(Razom_number__format__id__in = request.session['filterFormat'])
                    paramFormat = FormatPlanes.objects.filter(id__in=request.session['filterFormat'])
                except:
                    paramFormat = None

                try:
                    dataAll = dataAll.filter(story__id__in = request.session['filterStory'])
                    paramStory = Story.objects.filter(id__in=request.session['filterStory'])
                except:
                    paramStory = None

                outCity = []
                for i in dataAll.values('Razom_number__city_standart').distinct():
                    outCity.append(CityPlanes.objects.get(id=i['Razom_number__city_standart']))

                outType = []
                for i in dataAll.values('Razom_number__type').distinct():
                    outType.append(TypePlanes.objects.get(id=i['Razom_number__type']))

                outFormat = []
                for i in dataAll.values('Razom_number__format').distinct():
                    outFormat.append(FormatPlanes.objects.get(id=i['Razom_number__format']))

                outStory = []
                for i in dataAll.values('story').distinct():
                    outStory.append(Story.objects.get(id=i['story']))

                CountAC = {
                    "AllAC": len(RkCompany.objects.filter(rk=int(request.session['currentOutAC']))),
                    "like" : len(RkCompany.objects.filter(rk=int(request.session['currentOutAC'])).filter(Grade=1)),
                    "Dislike": len(RkCompany.objects.filter(rk=int(request.session['currentOutAC'])).filter(Grade=2))
                }

                appFilter = {
                    "City": paramCity,
                    "Format": paramFormat,
                    "Type": paramType,
                    "Story": paramStory,
                    "Product": Rk.objects.get(id=request.session['currentOutAC'])

                }
                request.session['currentDataOut'] = list(dataAll.values())
                return render(request, self.template_name, {
                    "color": WorkFiels.colorFile("admin"),
                    'lenguage': request.COOKIES['lenguage'],
                    'MyAC': Rk.objects.filter(client__founder=request.user.id),
                    'CurrentAC': dataAll,
                    'filterCity': outCity,
                    'filterType': outType,
                    'filterFormat': outFormat,
                    'filterStory': outStory,
                    'Program': dataAll,
                    'tableNameHead': WorkFile.outLenguage("tableHead"),
                    "CountAboutAC": CountAC,
                    "ParamFilter": appFilter,
                    'TranslateBody': WorkFile.outLenguage("MainMapPage"),
                    'TranslateModalWindow': WorkFile.outLenguage("ModalWindow"),
                    'TranslateHead': WorkFile.outLenguage("HeadMain"),
                    'Reach': ReachCity.objects.filter(rk=int(request.session['currentOutAC']))
                })
            except Exception as e:
                print('Ошибка:\n', traceback.format_exc())
                return render(request, self.template_name, {
                    "color": WorkFiels.colorFile("admin"),
                    'lenguage': request.COOKIES['lenguage'],
                    'MyAC': Rk.objects.filter(client__founder=request.user.id),
                    'tableNameHead': WorkFile.outLenguage("tableHead"),
                    'TranslateBody': WorkFile.outLenguage("MainMapPage"),
                    'TranslateModalWindow': WorkFile.outLenguage("ModalWindow"),
                    'TranslateHead': WorkFile.outLenguage("HeadMain")
                })

        else:
            return HttpResponseRedirect(reverse_lazy('Enter'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            color = WorkFiels.colorFile("admin")
            return render(request, self.template_name,  {"color": color})
        else:
            return HttpResponseRedirect(reverse_lazy('Enter'))


class SettingAdmin(View):

    template_name = 'SettingAdmin.html'

    def get(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:#filter
            information = []
            try:
                request.COOKIES['lenguage']
            except:
                request.session['Currentpage'] = 'setting'
                return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))
            for i in Rk.objects.filter(client__founder__id = request.user.id):
                tmpCount = RkCompany.objects.filter(rk__RK = i.RK).count()
                information.append({"Inf" : i, "Count" : tmpCount})
            return render(request, self.template_name, {
                'Allagancy' : Allagancy.objects.all(),
                'client' : Client.objects.filter(founder=request.user.id),
                'AdvertsCompany' : information,
                'lenguage': request.COOKIES['lenguage'],
                'tableNameHeadUser': WorkFile.outLenguage("TableUser"),
                'BaseObjLen':  WorkFile.outLenguage("SettingPage"),
                'tableAC': WorkFile.outLenguage("TableAC"),
                'AllMyUser': PermisionUsersClient.objects.filter(client__founder=request.user.id),
                'CountAC': Rk.objects.filter(client__founder__id = request.user.id).count(),
            })

    def post(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:
            allAgancy = Allagancy.objects.all()
            return render(request, self.template_name, {'Allagancy' : allAgancy})