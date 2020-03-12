from django.urls import path, re_path, include
from .views.bow import BowListView, BowDetailView, BowCreateView, BowUpdateView, BowDeleteView
from .views.log_entry import LogEntryListView, LogEntryDetailView, LogEntryUpdateView, LogEntryCreateView
from .views.round import RoundCreateView, RoundUpdateView, RoundDeleteView
from .views.end import EndCreateView, EndUpdateView, EndDeleteView
from .views.site import HomeView, AboutView, ContactView
from .views.account import AccountProfileView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('about', AboutView.as_view(), name="about"),
    path('contact', ContactView.as_view(), name="contact"),
    path('profile', AccountProfileView.as_view(), name="profile" ),
    path('log-entries', LogEntryListView.as_view(), name="log-entry-list"),
    path('round/new', RoundCreateView.as_view(), name="round-new"),
    path('round/update/<int:pk>', RoundUpdateView.as_view(), name="round-update"),
    path('round/delete/<int:pk>', RoundDeleteView.as_view(), name="round-delete"),
    path('end/new', EndCreateView.as_view(), name="end-new"),
    path('end/update/<int:pk>', EndUpdateView.as_view(), name="end-update"),
    path('end/delete/<int:pk>', EndDeleteView.as_view(), name="end-delete"),
    path('log-entry/<int:pk>', LogEntryDetailView.as_view(), name="log-entry-detail"),
    path('log-entry/new', LogEntryCreateView.as_view(), name="log-entry-new"),
    path('log-entry/update/<int:pk>', LogEntryUpdateView.as_view(), name="log-entry-update"),
    path('bows', BowListView.as_view(), name="bow-list"),
    path('bow/new', BowCreateView.as_view(), name="bow-new"),
    path('bow/update/<int:pk>', BowUpdateView.as_view(), name="bow-update"),
    path('bow/details/<int:pk>', BowDetailView.as_view(), name="bow-detail"),
    path('bow/delete/<int:pk>', BowDeleteView.as_view(), name="bow-delete"),
]