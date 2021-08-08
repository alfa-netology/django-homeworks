import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK


@pytest.mark.django_db
def test_course_list(api_client, course_factory):
    course_factory(_quantity=3)
    url = reverse('courses-list')
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 3


