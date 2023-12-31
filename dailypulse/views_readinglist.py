from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView

)
from rest_framework.permissions import IsAuthenticated
from .models import  Reading_later
from .permissions import IsOwnerOrReadOnly
from .serializers import ReadingLaterSerializer


class CreateReadingList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    '''
    create reading list : body attributes  all exepet id
    '''
    queryset = Reading_later.objects.all()
    serializer_class = ReadingLaterSerializer

class DeleteReadingList(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    '''
    delete reading list : requeiring id in url
    '''
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Reading_later.objects.all()
    serializer_class = ReadingLaterSerializer

class GetReadingList(ListAPIView):
    permission_classes = [IsAuthenticated]
    '''
    get reading list : requiring user id in url
    '''
    serializer_class = ReadingLaterSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Reading_later.objects.filter(user_id=user_id )
