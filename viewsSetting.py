from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views import View
from .models import *
from django.contrib import messages
import traceback

class SettingUtils(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('setting'))

    def post(self, request, utils):
        if utils == "addClient":
            try:
                Client(
                    client = request.POST.get("name_client"),
                    agancy = Allagancy.objects.get(id = int(request.POST.get("agancy"))),
                    founder = User.objects.get(id = request.user.id)
                ).save()
            except:
                messages.success(request, 'Такой клиент существует')
            finally:
                return HttpResponseRedirect(reverse_lazy('setting'))
        elif utils == "addRk":
            try:
                Rk.objects.filter(
                        client=int(request.POST.get("nm_client"))
                        ).get(RK=request.POST.get("name_rk"))
            except:
                Rk(
                    RK=request.POST.get("name_rk"),
                    client=Client.objects.get(id=int(request.POST.get("nm_client")))
                ).save()
                messages.success(request, 'Рекламная компания добавлена!')
            else:
                messages.success(request, 'У данного клиента уже есть данная рекламная компания')
            finally:
                return HttpResponseRedirect(reverse_lazy('setting'))
        elif utils == "delete":
            try :
                forDelete = Client.objects.get(id=int(request.POST.get("nm_client")))
                forDelete.delete()
            finally:
                return HttpResponseRedirect(reverse_lazy('setting'))
        elif utils == "DeleteRK":
            try:
                Rk.objects.get()
            except Exception as e:
                print('Ошибка:\n', traceback.format_exc())
            finally:
                return HttpResponseRedirect(reverse_lazy('setting'))
        elif utils == "ChangeLenguage":
            request.session['Currentpage'] = "setting"
            request.session['inLenluage'] = request.POST.get('Len')
            return HttpResponseRedirect(reverse_lazy('ChangeLenguage'))
        else:
            raise Http404

class ThisRK(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('setting'))

    def post(self, request, utils, RK):
        if utils == "DeleteRK":
            try:
                Rk.objects.get(id = RK).delete()
            except Exception as e:
                print('Ошибка:\n', traceback.format_exc())
            finally:
                return HttpResponseRedirect(reverse_lazy('setting'))
        elif utils == "Choose":
            try:
                print("hello")
                request.session['SettingRKName'] = int(RK)
                return HttpResponseRedirect(reverse_lazy('CurrentRK'))
            except Exception as e:
                print('Ошибка:\n', traceback.format_exc())
                raise Http404
        else:
            raise Http404
