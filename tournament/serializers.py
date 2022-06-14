from rest_framework import serializers
from tournament.models import Tournament


class CustomTournamentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    amountUsers = serializers.IntegerField(default=0)
    isFinished = serializers.BooleanField(default=False)
    start_time = serializers.DateField()

    class Meta:
        model = Tournament
        fields = (
        'id', 'name', 'amountUsers', 'isFinished', 'start_time', 'loser', 'winner', 'winnerResult', 'loserResult')

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
