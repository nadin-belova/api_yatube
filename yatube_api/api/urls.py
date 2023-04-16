from rest_framework.authtoken import views
from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet


# routerv1 = routers.DefaultRouter()
# routerv1.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/', PostViewSet.as_view),
]
