from django.shortcuts import render
from . models import CompanyInfo   
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class CominfoListView(ListView):
    model = CompanyInfo
    # Assumes videos/templates/videos/video_list.html exists.
    # Show the video list in alphabetical order by title.
    queryset = CompanyInfo.objects.order_by('company')

class CominfoThumbsView(ListView):
    model = CompanyInfo            # Hook to the model (Data)
    # Below we specify a different template for this ListView.
    template_name = "cominfo/companyinfo_thumbs.html"
    #Alternative to using object_list in the template.
    context_object_name = 'CompanyInfo_thumbs'


    # Here is how we filter records
    def get_queryset(self):
        # Get only video records fom requested category (category_id passed in from videos/urls.py)
        return CompanyInfo.objects.filter(category_id = self.kwargs['category_id']).filter(is_active = True)

class CominfoDetailView(DetailView):
    model = CompanyInfo 
    # Assumes videos/templates/videos/video_detail.html exists.

class CominfoCreateView(SuccessMessageMixin, CreateView):
    model = CompanyInfo
    fields = ('company', 'ceo', 'description', 'website', 'stars_count', 'region', 'skill_level_id', 'is_active', )  # only editable fields !!
    # Assumes videos/templates/videos/video_form.html exists.
    # Send back to videolist on successful save
    success_message = "Company Added"
    success_url = reverse_lazy('cominfo-list')

class CominfoUpdateView(SuccessMessageMixin, UpdateView):
    model = CompanyInfo
    fields = ('company', 'ceo', 'description', 'website', 'stars_count', 'region', 'skill_level_id', 'is_active', )  # only editable fields !!
    # Assumes videos/templates/videos/video_form.html exists.
    # Send back to videolist on successful save
    success_message = "Company Saved"
    success_url = reverse_lazy('cominfo-list')

class CominfoDeleteView(SuccessMessageMixin, DeleteView):
    model = CompanyInfo
    # Assumes videos/templates/videos/video_confirm_delete.html exists.
    # Send back to videolist on successful save
    success_message = "Company Deleted"
    success_url = reverse_lazy('cominfo-list')


