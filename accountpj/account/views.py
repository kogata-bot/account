from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Member, Event, Payment


# Member
class ListMemberView(ListView):
    template_name = "member/list.html"
    context_object_name = "member_list"
    model = Member


class DetailMemberView(DetailView):
    template_name = "member/detail.html"
    model = Member


class CreateMemberView(CreateView):
    template_name = "member/create.html"
    model = Member
    fields = ("name", "membership_type")
    success_url = reverse_lazy("list-member")


class DeleteMemberView(DeleteView):
    template_name = "member/delete.html"
    model = Member
    success_url = reverse_lazy("list-member")


class UpdateMemberView(UpdateView):
    template_name = "member/update.html"
    model = Member
    fields = ("name", "membership_type")

    success_url = reverse_lazy("list-member")


# Event
def list_event_view(request):
    event_list = Event.objects.order_by("date")
    return render(request, "event/list.html", {"event_list": event_list})


class DetailEventView(DetailView):
    template_name = "event/detail.html"
    model = Event


class CreateEventView(CreateView):
    template_name = "event/create.html"
    model = Event
    fields = ("date", "participants", "member")
    success_url = reverse_lazy("list-event")


class DeleteEventView(DeleteView):
    template_name = "event/delete.html"
    model = Event
    success_url = reverse_lazy("list-event")


class UpdateEventView(UpdateView):
    template_name = "event/update.html"
    model = Event
    fields = ("date", "participants", "member")
    success_url = reverse_lazy("list-event")


# Payment
def list_payment_view(request):
    payment_list = Payment.objects.order_by("event")
    return render(request, "payment/list.html", {"payment_list": payment_list})


class DetailPaymentView(DetailView):
    template_name = "payment/detail.html"
    model = Payment


class CreatePaymentView(CreateView):
    template_name = "payment/create.html"
    model = Payment
    fields = (
        "unit_teach_price",
        "unit_room_price",
        "room_price",
        "extra_income",
        "extra_outgo",
        "memo",
        "event",
    )
    success_url = reverse_lazy("list-payment")


class DeletePaymentView(DeleteView):
    template_name = "payment/delete.html"
    model = Payment
    success_url = reverse_lazy("list-payment")


class UpdatePaymentView(UpdateView):
    template_name = "payment/update.html"
    model = Payment
    fields = (
        "unit_teach_price",
        "unit_room_price",
        "room_price",
        "extra_income",
        "extra_outgo",
        "memo",
        "event",
    )
    success_url = reverse_lazy("list-payment")
