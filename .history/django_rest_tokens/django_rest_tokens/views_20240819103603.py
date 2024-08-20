from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def register(request):
    print(request.data)
    return Response({})

@api_view(['POST'])
def profile(request):
    return Response({})
