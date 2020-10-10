from django.http import HttpResponse
from django.views import View


class TestCBV(View):
    def get(self, request, price):
        return HttpResponse('CBV'+ price)

    def post(self, request):
        pass
