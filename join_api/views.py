# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import Contact
# from .serializers import ContactSerializer
# from rest_framework.views import APIView

# @api_view(['POST'])
# def add_contact(request):
#     serializer = ContactSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ContactListView(APIView):
#     def get(self, request):
#         # Alle Kontakte aus der Datenbank holen
#         contacts = Contact.objects.all()
        
#         # Kontakte serialisieren
#         serializer = ContactSerializer(contacts, many=True)
        
#         # Rückgabe der Daten als JSON
#         return Response(serializer.data, status=status.HTTP_200_OK)

from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

# View für das Erstellen eines neuen Kontakts (POST)
class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

# View zum Abrufen aller Kontakte (GET)
class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
