from rest_framework import serializers

from .models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'birth_day',
            'instagram',
            'twitter',
            'telegram',
            'website'
        )
