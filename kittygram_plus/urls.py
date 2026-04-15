from django.urls import include, path

from rest_framework.routers import SimpleRouter


from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet


router = SimpleRouter()

router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='mycats')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),         # Базовые эндпоинты (users, me и т.д.)
    # path('auth/', include('djoser.urls.authtoken')), # Если используете Token Authentication
    path('auth/', include('djoser.urls.jwt')),  # Эндпоинты для JWT (create, refresh, verify)
]

