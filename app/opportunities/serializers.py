from rest_framework import serializers

from .models import Opportunity, Department,OpportunityRegister


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("name",)


class OpportunitySerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()
    posted_by = serializers.SerializerMethodField()

    def get_posted_by(self, obj):
        return obj.posted_by.email

    def get_department(self, obj):
        return obj.department.name

    class Meta:
        model = Opportunity
        fields = "__all__"


class OpportunityRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityRegister
        fields = "__all__"
