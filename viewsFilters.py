from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views import View


class OutputWindow:

    @staticmethod
    def numberIn(text):
        outList = []
        for i in (str(text).replace("\n", " ")).split():
            outList.append(i.strip())
        return outList

class Filter(View):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse_lazy('Autentificate'))

    def post(self, request, type):
        if type == "city":
            request.session['filterCity'] = request.POST.getlist('for_city')
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        elif type == "ChooseRK":
            try:
                del request.session['currentOutAC']
            except:
                pass
            try:
                del request.session['filterCity']
            except:
                pass
            try:
                del request.session['filterType']
            except:
                pass
            try:
                del request.session['filterFormat']
            except:
                pass
            try:
                del request.session['advancedSearchType']
            except:
                pass
            try:
                del request.session['advancedSearchCodes']
            except:
                pass
            request.session['currentOutAC'] = request.POST.get('ch_rk')
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        elif type == "type":
            request.session['filterType'] = request.POST.getlist('for_type')
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        elif type == "format":
            request.session['filterFormat'] = request.POST.getlist('for_format')
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        elif type == "StoryFilter":
            request.session['filterStory'] = request.POST.getlist('point')
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        elif type == "ResetFilter":
            try:
                del request.session['filterCity']
            except:
                pass
            try:
                del request.session['filterType']
            except:
                pass
            try:
                del request.session['filterStory']
            except:
                pass
            try:
                del request.session['filterFormat']
            except:
                pass
            try:
                del request.session['advancedSearchType']
            except:
                pass
            try:
                del request.session['advancedSearchCodes']
            except:
                pass
            try:
                del request.session['currentDataOut']
            except:
                pass
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        elif type == "AdvandcedSearch":
            try:
                del request.session['filterCity']
            except:
                pass
            try:
                del request.session['filterType']
            except:
                pass
            try:
                del request.session['filterFormat']
            except:
                pass
            try:
                del request.session['currentDataOut']
            except:
                pass
            request.session['advancedSearchType'] = request.POST.get('search')
            request.session['advancedSearchCodes'] = OutputWindow.numberIn(request.POST.get("big_search"))
            return HttpResponseRedirect(reverse_lazy('Autentificate'))
        else:
            raise Http404