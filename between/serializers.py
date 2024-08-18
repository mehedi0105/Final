from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import update_session_auth_hash

User = get_user_model()

user_type = (
    ('seller','seller'),
    ('buyer','buyer'),
)

class RegistrationSerializer(serializers.ModelSerializer):
    account_type = serializers.ChoiceField(choices = user_type)
    confirm_password = serializers.CharField(required = True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','account_type','password','confirm_password']

    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        account_type = self.validated_data['account_type']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error':"password doesn't mactched"})
        
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error':'this email already exits pleace use diffarent email adress'})
        
        account = User(username = username,email=email, first_name = first_name, last_name= last_name, account_type = account_type)


        account.set_password(password)
        account.save()
        return account


class GetUserNameSerialzers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','account_type']




class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate_new_password1(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data

    def save(self):
        user = self.context['request'].user
        if not user.check_password(self.validated_data['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})
        user.set_password(self.validated_data['new_password1'])
        user.save()
        update_session_auth_hash(self.context['request'], user)
        return user