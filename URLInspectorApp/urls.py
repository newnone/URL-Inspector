from django.conf.urls import url

from . import views

app_name = "url_inspector"

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^pre_new_inspection", views.PreNewInspectionView.as_view(), name="pre_new_inspection"),
    url(r"^inspection/(?P<pk>\d+)", views.InspectionView.as_view(), name="inspection"),
    url(r"^inspections$", views.SavedInspectionsView.as_view(), name="inspections_saved"),
]
