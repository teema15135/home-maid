from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Maid
from .forms import MaidForm


class MaidListView(View):
    template_name = 'maid_list.html'
    
    def get(self, request):
        context = {
            'maid_list': Maid.objects.all()
        }
        return render(request, self.template_name, context)

class MaidAddView(View):
    template_name = 'maid_add.html'

    def get(self, request):
        form = MaidForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = MaidForm(request.POST)
        if form.is_valid:
            form.save()
        # print(form.errors())

        send_mail(
            'Subject here',
            'Here is the message',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False
        )
        return HttpResponse()


class MaidListAPIView(APIView):
    def get(self, request):
        return Response()


def maid_another_list_view(request):
    print(dir(request))
    template_name = 'maid_list.html'
    context = {
        'maid_list': Maid.objects.all()
    }
    return render(request, template_name, context)