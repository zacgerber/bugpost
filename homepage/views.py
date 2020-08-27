from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from homepage.models import Ticket
from homepage.forms import TicketForm


# Create your views here.


def index(request):
    html = "homepage.html"
    my_ticket = Ticket.objects.all()
    return render(request, html, {"my_ticket": my_ticket})


def ticket_detail_view(request, ticket_id):
    html = "ticket_detail.html"
    ticket_detail = Ticket.objects.filter(id=ticket_id).first()
    return render(request, html, {"ticket": ticket_detail})





# def author_detail(request, post_id):
#     html = "author_detail.html"
#     my_author = Author.objects.filter(id=post_id).first()
#     my_recipe = Ticket.objects.filter(author=my_author.id)
#     return render(request, html, {"post": my_author, "recipes": my_recipe})
#
#
# @login_required
# def ticket_form_view(request):
#     if request.method == "POST":
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Ticket.objects.create(
#                 title=data.get('title'),
#                 body=data.get('body'),
#                 instructions=data.get('instructions'),
#                 time_required=data.get('time_required'),
#                 author=data.get('author'),
#             )
#             return HttpResponseRedirect(reverse("homepage"))
#             # return HttpResponseRedirect(reverse("recipeview", args=[new_recipe.id]))
#
#     form = TicketForm()
#     return render(request, "basic_form.html", {"form": form})
#
#
# @login_required
# def ticket_edit_form(request, post_id):
#     if request.method == "POST":
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             return HttpResponseRedirect(reverse("homepage"))
#
#     form = TicketForm()
#     return render(request, "basic_form.html", {"form": form})


# @login_required
# def author_form_view(request):
#     if request.user.is_staff:
#
#         if request.method == "POST":
#             form = AuthorForm(request.POST)
#             if form.is_valid():
#                 data = form.cleaned_data
#                 new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
#                 Author.objects.create(name=data.get("username"), user=new_user)
#                 return HttpResponseRedirect(reverse("homepage"))
#     else:
#         return HttpResponse("Dont have proper credentials return home")
#     form = AuthorForm()
#     return render(request, "basic_form.html", {"form": form})
