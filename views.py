from django.contrib.auth import login, authenticate, logout
from django.db.models import Max
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from .models import *
from .AppFiles.LengualeOut import WorkFile
from .WorkFile import BodyWork


class EnterView(View):
    template_name = 'Enter.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:
            try:
                lenguage = request.COOKIES['lenguage']
            except:
                lenguage = "RU"
            return render(request, self.template_name, {
                'LengObj': WorkFile.outLenguage("EnterPage"),
                'lenguage': lenguage
            })

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:
            username = request.POST.get("username")
            password = request.POST.get("password")
            flagAuth = authenticate(username=username, password=password)
            if flagAuth is not None:
                login(request, flagAuth)
                return HttpResponseRedirect(reverse_lazy('Autentificate'))
            else:
                try:
                    lenguage = request.COOKIES['lenguage']
                except:
                    lenguage = "RU"
                return render(request, self.template_name, {
                    'error' : 'Не верный логин или пароль',
                    'LengObj': WorkFile.outLenguage("EnterPage"),
                    'lenguage': lenguage
                })

class ChangeLengEnterPage(View):

    def post(self, request):
        request.session['Currentpage'] = "Enter"
        request.session['inLenluage'] = request.POST.get('Len')
        return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))



class UpdateDoorsPage(View):
    template_name = 'UpdateData.html'

    def get(self, request):
        if request.user.is_staff:
            instatceNew = Totalplanes.objects.filter(Razom_number__lte= 99999).aggregate(Max('Razom_number'))
            return render(request, self.template_name, {
                'max': instatceNew['Razom_number__max'],
                'out': ""
            })
        return HttpResponseRedirect(reverse_lazy('Autentificate'))

    def post(self, request):
        if request.user.is_staff:
            emptyDoors = []
            request.FILES['userfile'].name = 'Update.xlsx'
            Excel = BodyWork(request.FILES['userfile'])
            Excel.chooseSheet('start')
            k = 2
            while True:
                if Excel.getElement(f'A{k}') == None:
                    break
                try:
                    instanceReady = Totalplanes.objects.get(doors=str(Excel.getElement(f'A{k}')))
                    instanceReady.OTS = Excel.getElement(f'B{k}')
                    instanceReady.GRP = Excel.getElement(f'C{k}')
                    instanceReady.save()
                except:
                    emptyDoors.append(Excel.getElement(f'A{k}'))
                k += 1




            return render(request, self.template_name, {
                'max' : 1,
                'out': emptyDoors
            })
        return HttpResponseRedirect(reverse_lazy('Autentificate'))


class NavigationPermision(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            if user.is_staff:
                return HttpResponseRedirect(reverse_lazy('UpdateDoorsGo'))
            try:
                groupName = str(user.groups.all()[0])
            except:
                raise Http404
            try:
                request.COOKIES['lenguage']
            except:
                request.session['Currentpage'] = "Autentificate"
                return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))

            if groupName == "Managers":
                return HttpResponseRedirect(reverse_lazy('Admin'))
            elif groupName == "UserSimply":
                return HttpResponseRedirect(reverse_lazy('Client'))
            else:
                raise Http404
        else:
            return HttpResponseRedirect(reverse_lazy('Enter'))

class LogOut(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('Enter'))

    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('Enter'))



# Create your views here.
