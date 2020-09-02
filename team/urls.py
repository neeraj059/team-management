"""teams URL Configuration
"""

from rest_framework import routers

from team.views import TeamMemberViewSet


router = routers.DefaultRouter()
router.register(r'teams', TeamMemberViewSet)

urlpatterns = router.urls

