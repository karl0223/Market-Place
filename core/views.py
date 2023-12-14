from django.shortcuts import redirect, render, get_object_or_404

from item.models import Category, Item
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold="False")[0:6]
    categories = Category.objects.all()
    return render(
        request, "core/index.html", context={"categories": categories, "items": items}
    )


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignupForm()

    return render(request, "core/signup.html", {"form": form})


def login(request):
    return render(request, "core/login.html")


def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    items = Item.objects.filter(is_sold="False", category=category)[0:6]
    categories = Category.objects.all()

    return render(
        request,
        "core/category_items.html",
        context={"categories": categories, "items": items},
    )
