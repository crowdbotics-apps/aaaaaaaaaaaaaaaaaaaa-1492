from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomTextViewSet,
    FDRFViewSet,
    HomePageViewSet,
    R1ViewSet,
    R5ViewSet,
    R56ViewSet,
    R57ViewSet,
    R6ViewSet,
    XXX1ViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
    AppReportView,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("r1", R1ViewSet)
router.register("r5", R5ViewSet)
router.register("r6", R6ViewSet)
router.register("r56", R56ViewSet)
router.register("r57", R57ViewSet)
router.register("xxx1", XXX1ViewSet)
router.register("fdrf", FDRFViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("report", AppReportView.as_view(), name="app_report"),
]
