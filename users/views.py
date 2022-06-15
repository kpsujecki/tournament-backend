from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NewUser
from .serializers import CustomUserSerializer, showProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ShowProfile(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = showProfileSerializer(request.user)
        return Response(serializer.data)


class GetUsers(ListAPIView):

    def get(self, request):
        queryset = User.objects.all()
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(serializer.data)


