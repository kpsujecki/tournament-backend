from django.contrib.auth import get_user_model
from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from tournament.models import Tournament
from tournament.serializers import CustomTournamentSerializer
from users.serializers import CustomUserSerializer

User = get_user_model()


class TournamentCreate(APIView):
    @staticmethod
    def post(request, format='json'):
        data = request.data
        new_tournament = Tournament.objects.create(name=data["name"], amountUsers=data["amountUsers"],
                                                   start_time=data["start_time"])
        new_tournament.save()

        for user in data["users"]:
            user_obj = User.objects.get(email=user["email"])
            user_obj.tournaments.add(new_tournament)

        serializer = CustomTournamentSerializer(new_tournament)
        return Response(serializer.data)


class GetActiveTournament(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Tournament.objects.filter(isFinished=False)
        serializer = CustomTournamentSerializer(queryset, many=True)
        return Response(serializer.data)


class GetFinishedTournament(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Tournament.objects.filter(isFinished=True)
        serializer = CustomTournamentSerializer(queryset, many=True)
        return Response(serializer.data)


class GetOneTournament(APIView):

    def get(self, request, *args, **kwargs):
        id = request.query_params["id"]
        if id is not None:
            tournament = Tournament.objects.get(id=id)
            users = User.objects.filter(tournaments=id)
            serializeUser = CustomUserSerializer(users, many=True)
            serializer = CustomTournamentSerializer(tournament)
            obj = [serializer.data, serializeUser.data, ]
        return Response(obj)

    def delete(self, request, *args, **kwargs):
        id = request.query_params["id"]
        if id is not None:
            Tournament.objects.get(id=id).delete()
        return Response('Remove tournament!')


class FinishTournament(APIView):
    def put(self, request, *args, **kwargs):
        id = request.query_params["id"]
        if id is not None:
            obj = Tournament.objects.get(id=id)
            obj.winner = request.data["winner"]
            obj.loser = request.data["loser"]
            obj.loserResult = request.data["loserResult"]
            obj.winnerResult = request.data["winnerResult"]
            obj.isFinished = True
            obj.save()
        return Response('Tournament has been ended')
