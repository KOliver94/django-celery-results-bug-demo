from rest_framework import serializers
from rest_framework.fields import CharField


class PollsSerializer(serializers.Serializer):
    name = CharField(max_length=150)
