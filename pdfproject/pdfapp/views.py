from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from weasyprint import HTML
from .serializers import PDFSerializer

# Create your views here.


class GeneratePDFView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PDFSerializer(data=request.data)
        if serializer.is_valid():
            context = serializer.validated_data

            html_string = render_to_string("pdf_template.html", context)

            pdf = HTML(string=html_string).write_pdf()

            response = HttpResponse(pdf, content_type="application/pdf")
            response["Content-Disposition"] = "inline; filename='document.pdf'"
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
