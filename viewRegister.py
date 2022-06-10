from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .AppFiles.LengualeOut import WorkFile
from .models import *
from django.contrib import messages
import traceback
from .AppFiles.EnterForm import EnterInSystem
from django.contrib.auth.models import Group

class RegisterPage(View):

    template_name = 'RegisterPage.html'

    def get(self,request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:
            try:
                request.COOKIES['lenguage']
            except:
                request.session['Currentpage'] = 'setting'
                return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))
            return render(request, self.template_name, {
                'client' : Client.objects.filter(founder=request.user.id),
                'lenguage': request.COOKIES['lenguage'],
                'LengObj': WorkFile.outLenguage("EnterPage")
            })

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:
            try:
                request.COOKIES['lenguage']
            except:
                request.session['Currentpage'] = 'setting'
                return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))
            try:
                DataValid = EnterInSystem.createUser(request.POST.get('brend'))
                print(DataValid)
                NewUser = User.objects.create_user(DataValid['Login'], 'example@mymail.com', DataValid['Password'])
                addUsergroup = Group.objects.get(id=2)
                addUsergroup.user_set.add(NewUser)
                NewAccClient = PermisionUsersClient(
                    client=Client.objects.get(id=request.POST.get('brend')),
                    userId = NewUser
                )
                NewAccClient.save()
            except Exception as e:
                DataValid = None
                print(traceback.format_exc())
            return render(request, self.template_name, {
                'client': Client.objects.filter(founder=request.user.id),
                'lenguage': request.COOKIES['lenguage'],
                'Form' : DataValid,
                'LengObj': WorkFile.outLenguage("EnterPage")
            })


class BackToSetting(View):
    def post(self,request):
        return HttpResponseRedirect(reverse_lazy('setting'))