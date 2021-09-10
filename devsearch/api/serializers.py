from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile



class ReviewSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProfileSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'



class TagSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class ProojectSeriliazer(serializers.ModelSerializer):
    owner = ProfileSeriliazer(many=False)
    tags = TagSeriliazer(many=True)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__' 

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSeriliazer(reviews, many=True)
        return serializer.data
