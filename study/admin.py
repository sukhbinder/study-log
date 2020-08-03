from django.contrib import admin

# Register your models here.
from study.models import StudyLog, Subject
admin.site.register(Subject)
admin.site.register(StudyLog)

