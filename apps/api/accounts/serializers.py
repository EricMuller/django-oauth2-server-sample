from rest_framework import serializers


class BasicUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()

    class Meta:
        fields = ('name', 'email')
