from rest_framework import serializers
from apps.app import models

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = (
            'id',
            'description',
            'ready',
            'user'
        )
    
    def create(self, validate_data):
        if not self.context['request'].user.is_anonymous:
            validate_data['user'] = self.context['request'].user
            instance = super().create(validate_data)
            return instance
        raise serializers.ValidationError({'error': 'El usuario debe estar autenticado'})


