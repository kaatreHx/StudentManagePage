from rest_framework import serializers
from .models import StudentData

class StudentDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)
    contact = serializers.IntegerField()
    semester = serializers.CharField(max_length=50)

    def create(self, validate_data):
        return StudentData.objects.create(**validate_data)
    
    def update(self, instance, validated_data):
        """
        Update an existing instance of StudentData with the provided validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.semester = validated_data.get('semester', instance.semester)

        instance.save()  # Save the updated instance to the database
        return instance