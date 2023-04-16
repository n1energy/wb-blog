from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model
from users.models import SubscribtionUser


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribtionUser
        fields = ("id", "subscriber")


class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscribtionUser
        fields = ("id", "user")


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=5, write_only=True)
    num_articles = serializers.IntegerField(read_only=True)
    authors = serializers.SerializerMethodField()
    subscribers = serializers.SerializerMethodField()

    def get_authors(self, obj):
        return AuthorsSerializer(obj.authors.all(), many=True).data

    def get_subscribers(self, obj):
        return SubscribersSerializer(obj.subscribers.all(), many=True).data

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "num_articles", "authors", "subscribers")


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class SubscriptionUserSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    subscriber = serializers.IntegerField()

    class Meta:
        model = SubscribtionUser
        # read_only_fields = ["user", "subscriber"]
        fields = ["user", "subscriber"]

    # def validate(self, args):
    #     user = args.get('user', None)
    #     subscriber = args.get('subscriber', None)
    #     if user == subscriber:
    #         raise serializers.ValidationError({'error': ('cant subscribe to yourself')})
    #     if SubscribtionUser.objects.filter(user=user, subscriber=subscriber).exists():
    #         raise serializers.ValidationError({'error': ('already subscribed')})
    #     return super().validate(args)

    # def create(self, validated_data):
    #     return SubscribtionUser.objects.create_user(**validated_data)


class UserFollowingSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    subscriber = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    
    class Meta:
        model = SubscribtionUser
        fields = ["user", "subscriber"]
        read_only_fields = ["user"]

    # def create(self, validated_data):
    #     instance = SubscribtionUser(
    #         **validated_data,
    #         user=self.context['kwargs']['pk'],
    #         subscriber=self.context['request']['user'],
    #     )
    #     return instance

