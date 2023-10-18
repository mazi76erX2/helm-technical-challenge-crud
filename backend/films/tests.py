import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Film


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_film_list_view(api_client):
    url = reverse("film_list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_film_detail_view(api_client):
    film = Film.objects.create(title="Film 1")
    url = reverse("film_detail", args=[film.pk])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_film_create_view(api_client):
    url = reverse("film_create")
    data = {"title": "New Film"}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_film_update_view(api_client):
    film = Film.objects.create(title="Film 1")
    url = reverse("film_update", args=[film.pk])
    data = {"title": "Updated Film"}
    response = api_client.put(url, data)
    assert response.status_code == status.HTTP_200_OK
    film.refresh_from_db()
    assert film.title == "Updated Film"


@pytest.mark.django_db
def test_film_delete_view(api_client):
    film = Film.objects.create(title="Film 1")
    url = reverse("film_delete", args=[film.pk])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Film.objects.filter(pk=film.pk).exists()
