# join_api/urls.py
# from django.urls import path
# from .views import add_contact, ContactListView

# urlpatterns = [
#     path('add_contact/', add_contact, name='add-contact'),  # POST zum Hinzufügen von Kontakten
#     path('contacts/', ContactListView.as_view(), name='contact-list'),  # GET zum Abrufen der Kontakte
# ]

from django.urls import path
from .views import ContactCreateView, ContactListView, ContactDetailView

urlpatterns = [
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('add_contact/', ContactCreateView.as_view(), name='add-contact'),  # POST zum Hinzufügen von Kontakten
    path('contacts/', ContactListView.as_view(), name='contact-list'),  # GET zum Abrufen der Kontakte
]
