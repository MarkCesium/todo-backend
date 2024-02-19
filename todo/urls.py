from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

router = DefaultRouter()
router.register("api/todo", viewset=TodoViewSet, basename="todo")
urlpatterns = router.urls
