from rest_framework import serializers
from projects.models import Project, Tag
from users.models import Profile


class ProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class TagSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class ProojectSeriliazer(serializers.ModelSerializer):
    owner = ProfileSerilizer(many=False)
    class Meta:
        model = Project
        fields = '__all__' 
