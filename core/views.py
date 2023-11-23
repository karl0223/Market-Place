from django.shortcuts import render

from item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold="False")[0:6]
    categories = Category.objects.all()
    return render(
        request, "core/index.html", context={"categories": categories, "items": items}
    )


def contact(request):
    return render(request, "core/contact.html")


def login(request):
    return render(request, "core/login.html")


def signup(request):
    return render(request, "core/signup.html")
