from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Moviedata
        # fields = ['name', 'duration', 'rating', 'typ', 'image']
        fields = '__all__'