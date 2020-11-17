from django.http import request
from asterisk_app.forms import ButtonForm
from django.views.generic.edit import FormView
from django.shortcuts import render
from asterisk_app.ami import connect_asterisk


class ButtonView(FormView):
    template_name = 'start.html'
    form_class = ButtonForm


def button(request):
    if request.GET.get('start'):
        return render(request, 'start.html', connect_asterisk())
