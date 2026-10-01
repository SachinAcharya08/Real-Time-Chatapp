from rest_framework import routers
from .views import ThreadViewset,MessageViewset

router=routers.DefaultRouter()
router.register('threads',ThreadViewset,basename='threads')
router.register('messages',MessageViewset,basename='messages')
urlpatterns = router.urls
