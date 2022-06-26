from rest_framework import serializers

from .models import UserModel, UserProfile, Hobby


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields= ["hobby_name"]
class UserProfileSerializer(serializers.ModelSerializer):
    get_hobbies = serializers.ListField(required = False)
    hobby = HobbySerializer(read_only=True, many=True)
    class Meta:
        model = UserProfile
        fields = ["address", "hobby", "get_hobbies"]
class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    def create(self, validated_data):
        user_profile = validated_data.pop('userprofile')
        get_hobbies = user_profile.pop('get_hobbies',[])
        password = validated_data.pop('password')
        new_user = UserModel(**validated_data)
        new_user.set_password(password)
        new_user.save()
        user_profile = UserProfile.objects.create(
            user= new_user,
            **user_profile
        )
        user_profile.hobby.add(*get_hobbies)
        return new_user
    class Meta:
        model = UserModel
        fields = ["email", "password", "nickname","fullname", "userprofile",]
        extra_kwargs = {
            "password" : {"write_only" : True}
        }