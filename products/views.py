from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cameralar
from .forms import ProductForm


class CameraListView(ListView):
    model = Cameralar
    template_name = 'products_list.html'  
    context_object_name = 'products'  


class CameraDetailView(DetailView):
    model = Cameralar
    template_name = 'product_detail.html'
    context_object_name = 'product'



class CameraCreateView(CreateView):
    model = Cameralar
    form_class = ProductForm  
    template_name = 'product_update.html'
    success_url = reverse_lazy('products_list') 



class CameraUpdateView(UpdateView):
    model = Cameralar
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'


class CameraDeleteView(DeleteView):
    model = Cameralar
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'
