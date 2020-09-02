# System and Django libraries

from rest_framework.throttling import AnonRateThrottle

from rest_framework import (
    status, permissions,
    viewsets
)
from rest_framework.response import Response

from team.models import TeamMembers
from team.serializers import TeamMembersSerializer


class TeamMemberViewSet(viewsets.ModelViewSet):
    """Views class for managing team members
    """
    permission_classes = (permissions.AllowAny,)

    queryset = TeamMembers.objects.all()

    serializer_class = TeamMembersSerializer
    """
    Throttled to 60 requests per minute based on setting DEFAULT_THROTTLE_RATES
    """
    throttle_classes = (AnonRateThrottle, )

    filter_fields = ['first_name', 'last_name', 'email', 'role', 'phone_number']
    search_fields = ['first_name', 'last_name', 'email', 'role', 'phone_number']
    ordering_fields = ['id', 'first_name', 'last_name', 'email', 'role',
                       'phone_number']

    def partial_update(self, request, pk=None):
        """
        :param request:
        :param pk:
        :return: updated fields on model team
        """
        try:
            instance = TeamMembers.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data='No data found for id: %s' % pk)
        serializer = TeamMembersSerializer(instance, data=request.data,
                                           partial=True,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK,
                        data=serializer.validated_data)
