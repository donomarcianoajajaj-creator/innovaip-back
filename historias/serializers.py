from rest_framework import serializers
from .models import Historia


class HistoriaPublicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['nombre', 'titulo', 'lugar_origen', 'tradicion', 'historia', 'personajes']


class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = '__all__'
        read_only_fields = ['fecha_envio']


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ['estado']
