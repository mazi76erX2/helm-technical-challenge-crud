from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import URLResolver, path
from .views import (
    FilmCreateView,
    FilmDeleteView,
    FilmDetailView,
    FilmListView,
    FilmUpdateView,
)

app_name: str = "films"

schema_view = get_schema_view(
    openapi.Info(
        title="Films API",
        default_version="v1",
        description="Films API with genre information",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mazi76erx@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns: list[URLResolver] = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("films/", FilmListView.as_view(), name="film_list"),
    path("films/<int:pk>/", FilmDetailView.as_view(), name="film_detail"),
    path("films/create/", FilmCreateView.as_view(), name="film_create"),
    path("films/<int:pk>/update/", FilmUpdateView.as_view(), name="film_update"),
    path("films/<int:pk>/delete/", FilmDeleteView.as_view(), name="film_delete"),
]
