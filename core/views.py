from django.shortcuts import render

from item.models import Category, Items


def index(request):
    items = Items.objects.filter(is_sold="False")[0:6]
    categories = Category.objects.all()
    return render(
        request, "core/index.html", context={"categories": categories, "items": items}
    )


def contact(request):
    return render(request, "core/contact.html")
