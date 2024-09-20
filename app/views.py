from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework import status
import uuid
import logging
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

logger = logging.getLogger(__name__)


# views.py
from rest_framework.response import Response
from rest_framework.views import APIView

class SalesData(APIView):
    def get(self, request, format=None):
        data = {
            "labels": ["January", "February", "March", "April", "May"],
            "sales": [100, 200, 150, 300, 250]
        }
        return Response(data)

# views.py
# from django.shortcuts import render

# def sales_chart(request):
#     return render(request, 'sales_chart.html')


@api_view(['GET'])
def comapnyviews(request):
    company_obj=Company.objects.all()
    serializers=CompanySerializer(company_obj,many=True)
    return Response(serializers.data)

# from django.shortcuts import render

# def sales_chart(request):
#     return render(request, 'sales_chart.html')
