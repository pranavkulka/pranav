from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

# class classname(View):
#     def get(self,request):
#         return HttpResponse("<h1>This is class based views</h1>")


# to external html page
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class myclass(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = 'login'  # Redirect to login page if not authenticated

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = f"Welcome, {self.request.user.username}!"
        return context


from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Company, Products

class Allcompanies(ListView):
    model = Company
    login_url = 'login'
    # template_name = 'index.html'  # your HTML template
    # context_object_name = 'companies'

    # def get_queryset(self):
    #     return Company.objects.prefetch_related('companies')


class CompanyDetails(DetailView):
    model = Company
    context_object_name = "mycompanies"
    login_url = 'login'

# class ProductDetails(DetailView):
#     model = Products
#     context_object_name = "myproducts"

class Allcompany(CreateView):
    model = Company
    fields='__all__'
    login_url = 'login' 

class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name', 'ceo', 'logo']
    login_url = 'login' 

from django.urls import reverse_lazy
class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('list')
    login_url = 'login' 
   