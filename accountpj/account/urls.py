from django.urls import path
from . import views

urlpatterns = [
    path("member/", views.ListMemberView.as_view(), name="list-member"),
    path(
        "member/<int:pk>/detail/",
        views.DetailMemberView.as_view(),
        name="detail-member",
    ),
    path("member/create/", views.CreateMemberView.as_view(), name="create-member"),
    path(
        "member/<int:pk>/delete/",
        views.DeleteMemberView.as_view(),
        name="delete-member",
    ),
    path(
        "member/<int:pk>/update/",
        views.UpdateMemberView.as_view(),
        name="update-member",
    ),
    path("event/", views.list_event_view, name="list-event"),
    path(
        "event/<int:pk>/detail/", views.DetailEventView.as_view(), name="detail-event"
    ),
    path("event/create/", views.CreateEventView.as_view(), name="create-event"),
    path(
        "event/<int:pk>/delete/", views.DeleteEventView.as_view(), name="delete-event"
    ),
    path(
        "event/<int:pk>/update/", views.UpdateEventView.as_view(), name="update-event"
    ),
    path("payment/", views.list_payment_view, name="list-payment"),
    path(
        "payment/<int:pk>/detail/",
        views.DetailPaymentView.as_view(),
        name="detail-payment",
    ),
    path("payment/create/", views.CreatePaymentView.as_view(), name="create-payment"),
    path(
        "payment/<int:pk>/delete/",
        views.DeletePaymentView.as_view(),
        name="delete-payment",
    ),
    path(
        "payment/<int:pk>/update/",
        views.UpdatePaymentView.as_view(),
        name="update-payment",
    ),
]
