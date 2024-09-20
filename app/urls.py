from django.urls import path
from .views import *


urlpatterns=[
    #  path('google/calendar/init/', GoogleCalendarInitView.as_view(), name='google_calendar_init'),
    # path('google/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='google_calendar_redirect'),
    # path('abcd/',InterviewQuestionView),
    # path('abcd/<int:pk>/',InterviewQuestionView),
    path('google/forms/init/', GoogleFormsInitView.as_view(), name='google_forms_init'),
    path('google/forms/redirect/', GoogleFormsRedirectView.as_view(), name='google_forms_redirect'),
    # path('google/forms/access/<uuid:token>/', AccessFormView.as_view(), name='access_form'),
     path('api/sales-data/', SalesData.as_view(), name='sales-data'),
    #  path('sales-chart/', sales_chart, name='sales-chart'),
     path('company/',comapnyviews)
 
]