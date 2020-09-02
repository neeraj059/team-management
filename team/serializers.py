"""team serializers
"""

from rest_framework import serializers, exceptions
from django.utils.translation import gettext as _

from team.models import TeamMembers


class TeamMembersSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        request = self.context['request']
        data = request.data
        valid_parameters = ['first_name', 'last_name', 'phone_number',
                            'email', 'role']
        for param in data:
            if param not in valid_parameters:
                message = _('%s is not a valid parameter' % param)
                _out = {
                    'status': 'FAIL',
                    'message': message
                }
                raise exceptions.ParseError(_out)

        if attrs.get('first_name') and attrs.get('last_name') \
                and attrs.get('first_name') == attrs.get('last_name'):
            raise serializers.ValidationError(
                "first_name and last_name shouldn't be same.")

        return attrs

    class Meta:
        model = TeamMembers
        fields = [
            'id', 'first_name', 'last_name',
            'phone_number', 'email', 'role'
        ]

