from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm


class TopView(TemplateView):
    template_name = "top.html"
    
# Productの一覧を表示するView
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "crud/product_list.html"
    paginate_by = 3

# Productの作成をするView
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'

# Productの追加をするView    
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
    
# Productの削除をするView
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('list')
    
# Productの詳細を表示するView
class ProductDetailView(DetailView):
    model = Product

# ログイン用のView
class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

# ログアウト用のView
class CustomLogoutView(LogoutView):
    template_name = 'top.html'