from rest_framework import routers
from store.views import PorductViewSet

router = routers.DefaultRouter()
router.register('produits', PorductViewSet)