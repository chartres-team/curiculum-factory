from django.shortcuts import render
# Create your views here.
from easy_pdf.views import PDFTemplateView

class HelloPDFView(PDFTemplateView):
    template_name = 'hello.html'