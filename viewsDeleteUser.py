from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views import View
from .models import *
import traceback

class DeleteUser(View):

    def post(self, request, idUser):
        try:
            userInstance = User.objects.get(id=idUser)
            userInstance.delete()
            return HttpResponseRedirect(reverse_lazy('setting'))
        except:
            return HttpResponseRedirect(reverse_lazy('setting'))