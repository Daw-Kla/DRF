from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
router.register('products-abc', ProductGenericViewSet, basename='products')

#witchout printing it out there is no clear way to see waht url genericViewSet uses
print(router.urls)
urlpatterns = router.urls