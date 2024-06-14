from rest_framework.routers import DefaultRouter

from .despesas import DespesasView

router = DefaultRouter()

# register your views
router.register(r'despesas', DespesasView, basename='teste')

urlpatterns = router.urls
