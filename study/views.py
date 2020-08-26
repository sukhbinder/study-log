from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from study.models import StudyLog
import pandas as pd

import io
import urllib, base64


class IndexListView(ListView):
    model = StudyLog
    template_name = "study/index.html"
    ordering = ['-date']



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


class StudyUpdateView(UpdateView):
    model = StudyLog
    template_name = "study/update_form.html"

    fields = "__all__"
  
    # can specify success url 
    # url to redirect after successfully 
    # updating details 
    success_url ="/"


def DashboardView(request):
    template_name = "dash.html"

    data = StudyLog.objects.all()
    data_list = [[d.date, d.user.lower(), str(d.subject).lower() , d.description] for d in data]
    df = pd.DataFrame(data_list, columns=["date", "user", "subject", "description"])

    df.set_index('date', inplace=True)

    # weeks = list(df.index.isocalendar().week.unique())
    # users  = list(df.user.unique())
    # subjects  = list(df.subject.unique())

    dd = df.groupby(["user"])
    # dd2 = df.groupby(["user",df.index.month]).count().unstack().fillna(0)
    # ddd = dd.to_dict("split")
    # ddd2 = dd2.to_dict("split")
    # df.to_csv("test.csv")
    # weeks = [i[1] for i in ddd["columns"]]
    
    # ddd = {g:i.subject.value_counts().to_dict() for g,i in dd}

    ddd=df.pivot_table(values="description", columns=["subject"], index=["user",df.index.weekofyear], aggfunc=lambda x: len(x.unique())).fillna(0).astype(int).to_html()  

    context = {"data": ddd}

    return render(request, template_name, context)