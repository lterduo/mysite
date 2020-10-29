from rest_framework import serializers
from api.models import User
from api.models import Role
from api.models import ProjectCategory

# class ApplicantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Applicant
#         fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'
