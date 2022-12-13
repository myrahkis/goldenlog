from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

import myapp.models as m
from .forms import *


def main_page_view(request, string="index"):
    print(string)
    category_list_dropdown = m.Categories.objects.all()
    product_list = m.Products.objects.all()
    name = "Категории"
    template_name = 'index.html'
    if string == 'index':
        template_name = 'index.html'
    elif string == 'Кухонный комплекс':
        template_name = 'categories/kitchen.html'
        product_list = m.Products.objects.filter(category__name=string)
    elif string == 'Комплект мебели для спальни':
        template_name = 'categories/bedroom.html'
        product_list = m.Products.objects.filter(category__name=string)
    elif string == 'Лампы':
        template_name = 'categories/lamps.html'
        product_list = m.Products.objects.filter(category__name=string)
    print(product_list.all())
    return render(request, template_name, {"headName": name, "catListDrop": category_list_dropdown, "prodList": product_list})


def login_view(request):
    return render(request, 'registration/login.html')


def register_view(request):
    return render(request, 'registration/register.html')


def about_info_view(request):
    category_list_dropdown = m.Categories.objects.all()
    return render(request, 'aboutInfo.html',  {"catListDrop": category_list_dropdown})


# def product_view(request, string="all"):
#     category_list_dropdown = m.Categories.objects.all()
#     name = "Категории"
#     if string == 'all':
#         product_list = m.Products.objects.all()
#     else:
#         product_list = m.Products.objects.filter(category__name=string)
#         name = string
#     return render(request, 'index.html', {"headName": name, "catListDrop": category_list_dropdown, "product_list": product_list})

#     category_list = m.Categories.objects.filter(name="Кухонный комплекс")
#     product_list = m.Products.objects.filter(category__name="Кухонный комплекс")
#     # elif string == 'kitchen':
#     #     category_list = m.Categories.objects.filter(name="Кухонный комплекс")
#     #     product_list = m.Products.objects.filter(category__name="Кухонный комплекс")
#     # elif string == 'bedroom':
#     #     category_list = m.Categories.objects.filter(name="Комплект мебели для спальни")  # через filter
#     #     product_list = m.Products.objects.filter(category__name="Комплект мебели для спальни")
#     # elif string == 'lamps':
#     #     category_list = m.Categories.objects.filter(name="Лампы")
#     #     product_list = m.Products.objects.filter(category__name="Лампы")
#     return render(request, 'index.html', )


# def kitchen_view(request):
#     category_list_dropdown = m.Categories.objects.all()
#     # category_list = m.Categories.objects.filter(name="Кухонный комплекс")
#     product_list = m.Products.objects.filter(category__name="Кухонный комплекс")
#
#     return render(request, 'categories/kitchen.html',
#                   {"prodList": product_list, "catListDrop": category_list_dropdown})
#
#
# def bedroom_view(request):
#     category_list_dropdown = m.Categories.objects.all()
#     # category_list = m.Categories.objects.filter(name="Комплект мебели для спальни")  # через filter
#     product_list = m.Products.objects.filter(category__name="Комплект мебели для спальни")
#
#     return render(request, 'categories/bedroom.html',
#                   {"prodList": product_list, "catListDrop": category_list_dropdown})
#
#
# def lamps_view(request):
#     category_list_dropdown = m.Categories.objects.all()
#     # category_list = m.Categories.objects.filter(name="Лампы")
#     product_list = m.Products.objects.filter(category__name="Лампы")
#
#     return render(request, 'categories/lamps.html',
#                   {"prodList": product_list, "catListDrop": category_list_dropdown})


@login_required
def creative_products_view(request):
    category_list_dropdown = m.Categories.objects.all()
    return render(request, 'creativeProducts.html', {"catListDrop": category_list_dropdown})


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = '/accounts/login'

    def form_valid(self, form):
        form.save()
        print(form.fields)
        return super().form_valid(form)


@login_required
def creative_order_view(request):
    category_list_dropdown = m.Categories.objects.all()
    form = CreativeOrderForm()

    if request.method == 'POST':
        form = CreativeOrderForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(id=request.user.id)
            obj.save()
            # print(form.cleaned_data)
            return redirect('home')
    return render(request, "creativeOrder.html", {'form': form, "catListDrop": category_list_dropdown})


@login_required
def user_info_view(request):
    category_list_dropdown = m.Categories.objects.all()
    return render(request, 'user/userInfo.html', {"catListDrop": category_list_dropdown})
