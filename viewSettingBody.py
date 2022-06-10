from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View

class TransmitSetting(View):
    def post(self, request):
        return HttpResponseRedirect(reverse_lazy('Register'))