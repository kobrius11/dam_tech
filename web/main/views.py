from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, View
from . import forms, utils

# Create your views here.
def index(request):
    return render(request, template_name="main/index.html")

class FormView(View):
    template_name = 'main/form_view.html'

    def get(self, request, *args, **kwargs):
        form = forms.Form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.Form(request.POST)
        if form.is_valid():
            # Process the form data as needed
            field1_value = form.cleaned_data['input_d_int']
            field2_value = form.cleaned_data['input_rd_int']

            request.session['form_data'] = {
                'darbuotoju_int': field1_value,
                'riboto_int': field2_value,
            }

            # Redirect to another URL with the form data
            return redirect('success_page') #field2=field2_value)

        return render(request, self.template_name, {'form': form})
    

def success_page(request):
    # Do something with the form data
    form_data = request.session.get('form_data', {})
    field1_value = int(form_data.get('darbuotoju_int', ''))
    field2_value = int(form_data.get('riboto_int', ''))


    result, advantage, x = utils.get_worker_percent(field1_value, field2_value)

    context = {'worker_percent': result, 'worker_advantage': advantage, 'x': x}
    return render(request, 'main/success_template.html', context)