from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from app.forms import *
# Create your views here.
'''class HtmlByTV(TemplateView):
    template_name='HtmlByTV.html' '''

class DatainsertByTV(TemplateView):
    template_name='DatainsertByTV.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        #ECDO['name']='Priya'
        #ECDO['age']=23
        ECDO['ECFO']=CollegeForm()
        return ECDO

    def post(self,request):
        CFDO=CollegeForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('Inserted is Done')
        else:
            return HttpResponse('Inserted is Failed')

class InsertDataByFV(FormView):
    template_name='InsertDataByFV.html'
    form_class=CollegeForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('Data is inserted')
