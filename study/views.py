from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from study.models import StudyLog

class IndexListView(ListView):
    model = StudyLog
    template_name = "study/index.html"
    order_by = "-date"


class LogCreationView(CreateView):
    model = StudyLog
    template_name = "study/create.html"

    fields= "__all__"

    success_url = "/"


class LogDetailView(DetailView):
    model = StudyLog
    template_name = "study/detail.html"


class UserListView(ListView):
    model = StudyLog
    template_name = "study/index.html"

    def get_queryset(self):
        user = self.kwargs['user']
        return StudyLog.objects.filter(user__iexact=user).order_by('-date')
