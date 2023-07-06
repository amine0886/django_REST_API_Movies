from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"
        
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields ="__all__"

# classs StreamPlatformSerializer(serializers.HyperlinkedModelSerializer)
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only=True)
      
    class Meta:
        model = StreamPlatform
        fields = "__all__"

        
           
    # def get_len_names(self, object):
    #     return len(object.name)
        
    # def validate(self, data):        
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title ans description shold be different!")
    #     else:
    #         return data
        
    # def validate_name(self, value):        
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is short!")
    #     else:
    #         return value   
        
         

# def name_length(value):        
#         if len(value) < 2:
#             raise serializers.ValidationError("name is short!")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     activate = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance ,validated_data):
#         instance.name = validated_data.get('name', instance.name) 
#         instance.description = validated_data.get('description', instance.description)
#         instance.activate = validated_data.get('activate', instance.activate)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title ans description shold be different!")
#         else:
#             return data
    
    # def validate_name(self, value):
        
    #     if len(value) < 2:
    #         raise serializers.ValidationError("name is short!")
    #     else:
    #         return value
        