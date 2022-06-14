"""tournament URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import TournamentCreate, GetActiveTournament, GetFinishedTournament,\
    GetOneTournament, FinishTournament


app_name = 'tournament'

urlpatterns = [
    path('create/tournament/', TournamentCreate.as_view(), name="tournament_create"),
    path('activeTournament/', GetActiveTournament.as_view(), name="tournament_active"),
    path('finishedTournament/', GetFinishedTournament.as_view(), name="tournament_finished"),
    path('getActiveOneTournament/', GetOneTournament.as_view(), name="get_one_active_tournament"),
    path('finishTournament/', FinishTournament.as_view(), name='finishTournament')

]
