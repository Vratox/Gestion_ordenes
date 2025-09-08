from rest_framework.routers import DefaultRouter
from .viewsets import OrdenViewSet

router = DefaultRouter()
router.register(r'ordenes', OrdenViewSet)

urlpatterns = router.urls
