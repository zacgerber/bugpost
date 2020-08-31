from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from homepage.models import Ticket
from homepage.forms import TicketForm
from bugpostapp.models import MyUser

# Create your views here.


def index(request):
    html = "homepage.html"
    my_ticket = Ticket.objects.all()
    return render(request, html, {"my_ticket": my_ticket})


def ticket_detail_view(request, ticket_id):
    html = "ticket_detail.html"
    ticket_detail = Ticket.objects.filter(id=ticket_id).first()
    return render(request, html, {"ticket": ticket_detail})


@login_required
def create_ticket_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data.get('title'),
                description=data.get('description'),
            )
            return HttpResponseRedirect(reverse("ticket_detail"))
            # return HttpResponseRedirect(reverse("recipeview", args=[new_recipe.id]))

    form = TicketForm()
    return render(request, "basic_form.html", {"form": form})


@login_required
def ticket_edit_view(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.description = data["description"]
            ticket.title = data["title"]
            ticket.user_assigned = data["user_assigned"]
            ticket.user_completed = data["user_completed"]
            ticket.ticket_status = data["ticket_status"]
            ticket.save()
        return HttpResponseRedirect(reverse("ticket_detail_view", args=[ticket.id]))

    data = {
        "title": ticket.title,
        "description": ticket.description
    }
    form = TicketForm(initial=data)
    return render(request, 'basic_form.html', {"form": form})


def in_progress_ticket_view(request, ticket_id):
    inprogress_ticket = Ticket.objects.filter(id=ticket_id)
    inprogress_ticket.status = 'INP'
    inprogress_ticket.user_assigned = request.user
    inprogress_ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_view', args=[inprogress_ticket.id]))


def completed_ticket_view(request, ticket_id):
    completed_ticket = Ticket.objects.filter(id=ticket_id)
    completed_ticket.status = 'D'
    completed_ticket.user_completed = request.user
    completed_ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_view', args=[completed_ticket.id]))


def invalid_ticket_view(request, ticket_id):
    invalid_ticket = Ticket.objects.filter(id=ticket_id)
    invalid_ticket.status = 'INV'
    invalid_ticket.user_completed = request.user
    invalid_ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail_view', args=[invalid_ticket.id]))


def user_detail_view(request, ticket_id):
    html = "user_detail.html"
    my_user = MyUser.objects.filter(id=ticket_id).first()
    my_tickets = Ticket.objects.filter(my_user=my_user.id)
    return render(request, html, {"user": my_user, "ticket": my_tickets})
