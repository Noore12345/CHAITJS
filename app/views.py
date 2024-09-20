from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def comapnyviews(request):
    company_obj=Company.objects.all()
    serializers=CompanySerializer(company_obj,many=True)
    return Response(serializers.data)

