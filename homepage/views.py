from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from homepage.models import Ticket
from homepage.forms import TicketForm
from bugpostapp.models import MyUser

# Create your views here.


@login_required
def index(request):
    html = "homepage.html"
    new_tickets = Ticket.objects.filter(ticket_status="N")
    in_progress_tickets = Ticket.objects.filter(ticket_status="IP")
    completed_tickets = Ticket.objects.filter(ticket_status="D")
    invalid_tickets = Ticket.objects.filter(ticket_status="INV")
    return render(request, html, {"New": new_tickets, "In_Progress": in_progress_tickets, "Completed": completed_tickets,
                                  "Invalid": invalid_tickets})


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
                user_filed=request.user
            )
            return HttpResponseRedirect(reverse("homepage"))

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
            ticket.save()
            return HttpResponseRedirect(reverse("ticket_detail", args=[ticket.id]))

    data = {
        "title": ticket.title,
        "description": ticket.description
    }
    form = TicketForm(initial=data)
    return render(request, 'basic_form.html', {"form": form})


def in_progress_ticket_view(request, ticket_id):
    inprogress_ticket = Ticket.objects.filter(id=ticket_id).first()
    inprogress_ticket.status = 'INP'
    inprogress_ticket.user_assigned = request.user
    inprogress_ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=[inprogress_ticket.id]))


def completed_ticket_view(request, ticket_id):
    completed_ticket = Ticket.objects.filter(id=ticket_id).first()
    completed_ticket.ticket_status = 'D'
    completed_ticket.user_completed = completed_ticket.user_assigned
    completed_ticket.user_assigned = None
    completed_ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=[completed_ticket.id]))


def invalid_ticket_view(request, ticket_id):
    invalid_ticket = Ticket.objects.filter(id=ticket_id).first()
    invalid_ticket.ticket_status = 'INV'
    invalid_ticket.user_completed = None
    invalid_ticket.user_assigned = None
    invalid_ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=[invalid_ticket.id]))


def user_detail_view(request, ticket_id):
    html = "user_detail.html"
    my_user = MyUser.objects.filter(id=ticket_id).first()
    filed_tickets = Ticket.objects.filter(user_filed=my_user)
    in_progress = Ticket.objects.filter(user_assigned=my_user)
    completed = Ticket.objects.filter(user_completed=my_user)
    return render(request, html, {"filed": filed_tickets, "in_progress": in_progress, "completed": completed})
