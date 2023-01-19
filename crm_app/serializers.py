from rest_framework import serializers
from .models import User, Employee, Vacation
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:

        model = User
        fields = ['email', 'name', 'password', 'phone',
                  'country', ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.country = validated_data.get('country', instance.country)
        password = make_password(instance.password)
        instance.password = password
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(max_length=20, required=True, validators=[
        UniqueValidator(queryset=Employee.objects.all(), message='This email already exists')])

    class Meta:
        model = Employee
        fields = ['name', 'email', 'password',
                  'description', 'phone', 'position']

    def create(self, validated_data):
        password = validated_data.pop('password')
        employee = Employee.objects.create(**validated_data)
        password = make_password(password)
        employee.password = password
        employee.save()
        return employee

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        password = make_password(instance.password)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.password = password
        instance.phone = validated_data.get('phone', instance.phone)
        instance.postion = validated_data.get('position', instance.position)
        instance.save()
        return instance


class VacationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacation
        fields = ['date', 'response']
