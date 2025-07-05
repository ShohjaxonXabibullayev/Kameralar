from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cameralar
from .forms import ProductForm


# Mahsulotlar ro'yxati
class CameraListView(ListView):
    model = Cameralar
    template_name = 'products_list.html'  # qaysi HTML faylga chiqadi
    context_object_name = 'products'  # {{ products }} orqali foydalaniladi


# Bitta mahsulotning tafsiloti
class CameraDetailView(DetailView):
    model = Cameralar
    template_name = 'product_detail.html'
    context_object_name = 'product'


# Mahsulot qo'shish
class CameraCreateView(CreateView):
    model = Cameralar
    form_class = ProductForm  # forms.py dan formani olib ishlatadi
    template_name = 'product_update.html'
    success_url = reverse_lazy('products_list')  # muvaffaqiyatli qo‘shilgandan keyin qayerga yo‘naltirish


# Mahsulotni tahrirlash
class CameraUpdateView(UpdateView):
    model = Cameralar
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'

# Mahsulotni o‘chirish
class CameraDeleteView(DeleteView):
    model = Cameralar
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product'