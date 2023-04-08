from rest_framework.routers import DefaultRouter
from .views import AccountView, BlogView, CommentView

router = DefaultRouter()

router.register(
    r"account",
    AccountView,
    basename="AccountView",
)

router.register(
    r"blog",
    BlogView,
    basename="BlogView",
)

router.register(
    r"comment",
    CommentView,
    basename="CommentView",
)
urlpatterns=[]

urlpatterns += router.urls