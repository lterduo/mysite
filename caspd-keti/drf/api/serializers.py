from rest_framework import serializers
from api.models import *


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


class ProjectCategorySonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategorySon
        fields = '__all__'


class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatus
        fields = '__all__'


class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = '__all__'


class ProjectLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLeader
        fields = '__all__'


class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = '__all__'


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileList
        fields = '__all__'


class AuditInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditInfo
        fields = '__all__'


class ProjectDistributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDistribute
        fields = '__all__'


class AssessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessor
        fields = '__all__'


class AssessorMajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessorMajor
        fields = '__all__'


class ProjectAssessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectAssess
        fields = '__all__'
