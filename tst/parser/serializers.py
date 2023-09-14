from rest_framework import serializers

class Rates:
    def __init__(self, result):
        self.result = result

class RatesSerializer(serializers.Serializer):
    result = serializers.CharField(max_length=255)