from rest_framework import serializers


class PDFSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=70)
    content = serializers.CharField()
    items = serializers.ListField(child=serializers.CharField(max_length=100))
