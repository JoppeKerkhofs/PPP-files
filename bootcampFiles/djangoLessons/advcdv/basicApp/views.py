from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basicApp.models import School, Student
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     return render(request, 'basicApp/index.html')

# class IndexView(View):
#     def get(self, request):
#         return render(request, 'basicApp/index.html')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection!'
        return context
    
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'basicApp/schoolList.html'

class SchoolDetailView(DetailView):
    model = School
    template_name = 'basicApp/schoolDetails.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('basicApp:list')