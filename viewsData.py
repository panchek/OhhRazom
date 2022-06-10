from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .AppFiles.OutColorFile import WorkFiels
from .models import *
from django.http import HttpResponseRedirect, Http404, HttpResponse

import traceback
from .PlaceApp import *
import os


class ImportDBCity(View):

    def get(self, request, *args, **kwargs):
        dataCity = WorkFiels.outToDB('Districcity')
        for i in dataCity:
            try:
                CityPlanes(
                    id=int(i),
                    city_standart_UA=dataCity[i]["UA"],
                    city_standart_RU=dataCity[i]["RU"],
                    city_standart_EN=dataCity[i]["EN"]
                ).save()
            except:
                print(dataCity[i]["RU"], " Уже есть")
        print("City Ready!")
        return HttpResponseRedirect(reverse_lazy('Side'))


class ImportDBSide(View):

    def get(self, request, *args, **kwargs):
        data = WorkFiels.outToDB('DistSide')
        for i in data:
            SidePlanes(
                id=int(i),
                side=str(data[i]),
            ).save()
        print("Side Ready!")
        return HttpResponseRedirect(reverse_lazy('Format'))


class ImportDBFormat(View):

    def get(self, request, *args, **kwargs):
        data = WorkFiels.outToDB('Districformat')
        for i in data:
            FormatPlanes(
                id=int(i),
                format=data[i],
            ).save()
        print("Format Ready!")
        return HttpResponseRedirect(reverse_lazy('Type'))


class ImportDBType(View):

    def get(self, request, *args, **kwargs):
        dataCity = WorkFiels.outToDB('Districtype')
        for i in dataCity:
            print(f'UA - {dataCity[i]["UA"]} RU - {dataCity[i]["RU"]} EN - {dataCity[i]["EN"]}')
            TypePlanes(
                id=int(i),
                typeUA=dataCity[i]["UA"],
                typeRU=dataCity[i]["RU"],
                typeEN=dataCity[i]["EN"]
            ).save()
        print("Type Ready!")
        return HttpResponseRedirect(reverse_lazy('Contactor'))


class ImportDBContactor(View):

    def get(self, request, *args, **kwargs):
        data = WorkFiels.outToDB('Districcontactor')
        for i in data:
            try:
                ContractorPlanes(
                    id=int(i),
                    Contractor_UA=data[i]["UA"],
                    Contractor_RU=data[i]["RU"],
                    Contractor_EN=data[i]["EN"]
                ).save()
            except:
                print(data[i]["RU"], " Уже есть")
        print("Contactor Ready!")
        return HttpResponseRedirect(reverse_lazy('Enter'))

class ImportDBadress(View):

    def get(self, request, *args, **kwargs):
        data = WorkFiels.outToDB('adress')
        for i in data:
            try:
                AdressPlanes(
                    id=int(i),
                    adress_UA=data[i]["UA"],
                    adress_RU=data[i]["RU"],
                    adress_EN=data[i]["EN"]
                ).save()
            except:
                print(int(i))
        print("Contactor Ready!")
        return HttpResponseRedirect(reverse_lazy('Enter'))

class ImportDBloc(View):

    def get(self, request, *args, **kwargs):
        data = WorkFiels.outToDB('loc')
        for i in data:
            try:
                LocationPlanes(
                    id=int(i),
                    Location_UA=data[i]["UA"],
                    Location_RU=data[i]["RU"],
                    Location_EN=data[i]["EN"]
                ).save()
            except:
                print(int(i))
        print("Contactor Ready!")
        return HttpResponseRedirect(reverse_lazy('Enter'))

class ImportDBFinall(View):

    def get(self, request, *args, **kwargs):
        data = WorkFiels.outToDB('finally')
        strPath = "D:\перевод сайт в\ooh"
        for i in data:
            if os.path.exists(os.path.join(strPath, "media", "OhhRazom", "image", "photo", f'{i["Razom_number"]}.jpg')):
                try:
                    Totalplanes(
                        lat=i["lat"],
                        lng=i["lng"],
                        doors=i["doors"],
                        Self_number=i["Self_number"],
                        Razom_number=i["Razom_number"],
                        type=TypePlanes.objects.get(id = i["type"]),
                        format=FormatPlanes.objects.get(id = i["format"]),
                        OTS=i["OTS"],
                        GRP=i["GRP"],
                        adress=AdressPlanes.objects.get(id = i["adress"]),
                        house=i["house"],
                        city_standart=CityPlanes.objects.get(id = int(i["city_standart"])),
                        side=SidePlanes.objects.get(id = i["side"]),
                        loc=LocationPlanes.objects.get(id = i["Loc"]),
                        Contractor=ContractorPlanes.objects.get(id = i["Contractor"]),
                        route=i["route"],
                        imagePhoto=f'OhhRazom/image/photo/{i["Razom_number"]}.jpg',
                        imageShema=f'OhhRazom/image/shema/{i["Razom_number"]}.jpg'
                    ).save()
                except Exception as e:
                    print("------" + str(i["Razom_number"]))
                    print('Ошибка:\n', traceback.format_exc())
            else:
                try:
                    Totalplanes(
                        lat=i["lat"],
                        lng=i["lng"],
                        doors=i["doors"],
                        Self_number=i["Self_number"],
                        Razom_number=i["Razom_number"],
                        type=TypePlanes.objects.get(id = i["type"]),
                        format=FormatPlanes.objects.get(id = i["format"]),
                        OTS=i["OTS"],
                        GRP=i["GRP"],
                        adress=AdressPlanes.objects.get(id = i["adress"]),
                        house=i["house"],
                        city_standart=CityPlanes.objects.get(id = int(i["city_standart"])),
                        side=SidePlanes.objects.get(id = i["side"]),
                        loc=LocationPlanes.objects.get(id = i["Loc"]),
                        Contractor=ContractorPlanes.objects.get(id = i["Contractor"]),
                        route=i["route"]
                    ).save()
                except Exception as e:
                    print("------" + str(i["Razom_number"]))
                    print('Ошибка:\n', traceback.format_exc())
        print("Finall Ready!")
        return HttpResponseRedirect(reverse_lazy('Enter'))


class FixProblem(View):

    def get(self,request):
        instanceTotal = Totalplanes.objects.filter(city_standart__city_standart_RU = 'Ужгород')
        for i in instanceTotal:
            i.imagePhoto=f'OhhRazom/image/photo/{i.Razom_number}.jpg'
            i.imageShema = f'OhhRazom/image/shema/{i.Razom_number}.jpg'
            i.save()
        return HttpResponseRedirect(reverse_lazy('Enter'))





