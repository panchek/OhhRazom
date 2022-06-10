from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View


class Lenguage(View):

    def get(self, request):
        response = HttpResponseRedirect(reverse_lazy(request.session['Currentpage']))
        response.set_cookie('lenguage', request.session.get('inLenluage', 'RU'),  365 * 24 * 60 * 60)
        return response