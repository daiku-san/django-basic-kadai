from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
    template_name = "top.html"
    
# Productの一覧を表示するView
class ProductListView(ListView):
    model = Product
    template_name = "crud/product_list.html"
    paginate_by = 3

# Productの作成をするView
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'

# Productの追加をするView    
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
    
# Productの削除をするView
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')

