from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"mails", views.MailViewSet)
router.register(r"recipients", views.RecipientViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = "api"
urlpatterns = [path("", include(router.urls))]
