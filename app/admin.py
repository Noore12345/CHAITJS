from django.contrib import admin
from .models import *

admin.site.register(OneTimeAccessToken)
admin.site.register(Company)
admin.site.register(Interview)
admin.site.register(Interviewer)
admin.site.register(InterviewPhase)
admin.site.register(InterviewQuestion)




admin.site.site_header="Admin Portal"
admin.site.index_title="Dashboard"
