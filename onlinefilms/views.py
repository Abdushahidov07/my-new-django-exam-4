from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy
# Create your views here.


class FilmsListView(ListView):
    model = Films
    template_name = "home.html"
    context_object_name = 'films'

class FilmsDetailView(DetailView):
    model = Films
    template_name = "films.html"
    context_object_name = 'film'
    
class FilmsCreateView(CreateView):
    model = Films
    template_name = "createfilm.html"
    fields = ("title", "category_id","descriptions","tikets","price","teatre","video","img","date_view")
    success_url = reverse_lazy('home')

class FilmsUpdateView(UpdateView):
    model = Films
    template_name = "updatefilm.html"
    fields = ("title", "category_id","descriptions","tikets","price","teatre","video","img","date_view")
    success_url = reverse_lazy('home')

class FilmsDeleteView(DeleteView):
    model = Films
    template_name = "deletefilm.html"
    success_url = reverse_lazy('home')
    context_object_name = 'film'





class CategoryListView(ListView):
    model = Category
    template_name = "allcategory.html"
    context_object_name = 'categorys'

class CategoryDetailView(DetailView):
    model = Category
    template_name = "detailcategory.html"
    context_object_name = 'category'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["films"] = Films.objects.filter(category_id = self.kwargs['pk'])
        return context
    
    
class CategoryCreateView(CreateView):
    model = Category
    template_name = "createcategory.html"
    fields = ("category_name",)
    success_url = reverse_lazy('allcategorys')
    # def form_valid(self, form):
    #     form.
    #     return super().form_valid(form)
    

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "updatecategory.html"
    fields = ("category_name",)
    success_url = reverse_lazy('allcategorys')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "deletecategory.html"
    success_url = reverse_lazy('allcategorys')




class TeatreListView(ListView):
    model = Teatre
    template_name = "allteatre.html"
    context_object_name = 'teatres'

class TeatreDetailView(DetailView):
    model = Teatre
    template_name = "detailteatre.html"
    context_object_name = 'teatre'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["films"] = Films.objects.filter(teatre = self.kwargs["pk"])
        return context
    
    
class TeatreCreateView(CreateView):
    model = Teatre
    template_name = "createteatre.html"
    fields = ("name_teatre", "city_id","region_id","street_id",)
    success_url = reverse_lazy('allteatre')


class TeatreUpdateView(UpdateView):
    model = Teatre
    template_name = "updateteatre.html"
    fields = ("name_teatre", "city_id","region_id","street_id",)
    success_url = reverse_lazy('allteatre')

class TeatreDeleteView(DeleteView):
    model = Teatre
    template_name = "deletefilm.html"
    context_object_name = 'teatre'
    success_url = reverse_lazy('allteatre')




class OrdersListView(ListView):
    model = Orders
    template_name = "allorders.html"
    context_object_name = 'orders'

class OrdersDetailView(DetailView):
    model = Orders
    template_name = "detailorders.html"
    context_object_name = 'order'

    

class OrdersCreateView(CreateView):
    model = Orders
    template_name = "createorder.html"
    fields = ("user_id", "qvantity", "type_pay")
    success_url = reverse_lazy('allorders')
    def form_valid(self, form):
        films = Films.objects.filter(id=self.kwargs["pk"]).first()
        if films:
            form.instance.film = films 
            return super().form_valid(form)  
        else:
            return self.form_invalid(form)

class OrdersUpdateView(UpdateView):
    model = Orders
    template_name = "updateorders.html"
    fields = ("user_id", "film","qvantity","type_pay",)
    success_url = reverse_lazy('allorders')


class OrdersDeleteView(DeleteView):
    model = Orders
    template_name = "deleteorders.html"
    success_url = reverse_lazy('allorders')
    context_object_name = "order"
