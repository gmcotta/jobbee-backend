from rest_framework import serializers
from .models import CandidatesApplied, Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class CandiatesAppliedSerializer(serializers.ModelSerializer):
    job = JobSerializer()
    class Meta:
        model = CandidatesApplied
        fields = ('user', 'resume', 'appliedAt', 'job')
