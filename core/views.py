from django.db.models.aggregates import Count
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from item.models import Category, Item
from .forms import SignupForm


def index(request):
    items_list = Item.objects.filter(is_sold=False)

    # Set the number of items to display per page
    items_per_page = 6

    # Create a Paginator object
    paginator = Paginator(items_list, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get("page")

    try:
        # Get the Page object for the requested page
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results.
        items = paginator.page(paginator.num_pages)

    categories = Category.objects.annotate(items_count=Count("items"))
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


def about(request):
    return render(request, "core/about.html")


def policy(request):
    return render(request, "core/policy.html")


def terms_of_use(request):
    return render(request, "core/tos.html")


def category_items(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    items_list = Item.objects.filter(is_sold="False", category=category)[0:6]

    # Set the number of items to display per page
    items_per_page = 6

    # Create a Paginator object
    paginator = Paginator(items_list, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get("page")

    try:
        # Get the Page object for the requested page
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page of results.
        items = paginator.page(paginator.num_pages)

    categories = Category.objects.annotate(items_count=Count("items"))

    return render(
        request,
        "core/category_items.html",
        context={"categories": categories, "items": items},
    )
