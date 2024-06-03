from rest_framework import serializers
from .models import Qurilish, Hudud, QurilishTashkiloti


class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = "__all__"
        

class QurilishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qurilish
        fields = "__all__"
        
        
class QurilishTashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishTashkiloti
        fields = "__all__"