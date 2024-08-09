from rest_framework import generics
from .models import Statement
from .serializers import StatementSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



class StatementListCreate(generics.ListCreateAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class StatementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "This is a protected view!"})
