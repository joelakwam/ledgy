from rest_framework import serializers
from .models import Statement

class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = '__all__'
