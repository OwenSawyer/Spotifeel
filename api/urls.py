from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views
from webpack_loader import utils

# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register(r'user', views.UserViewSet, base_name='user')
#router.register(r'record', views.RecordViewSet, base_name='record')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
print(utils.get_files('main'))
