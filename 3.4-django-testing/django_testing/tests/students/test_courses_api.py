import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_exercise_1(api_client, course_factory):
    # Arrange
    course = course_factory(_quantity=1)
    # Act
    response = api_client.get("/api/v1/courses/")
    # Assert
    data = response.json()
    assert data[0]['name'] == course[0].name
    assert response.status_code == 200


@pytest.mark.django_db
def test_exercise_2(api_client, course_factory):
    # Arrange
    course = course_factory(_quantity=20)
    # Act
    response = api_client.get("/api/v1/courses/")
    # Assert
    data = response.json()
    assert response.status_code == 200
    for i, n in enumerate(data):
        assert n['name'] == course[i].name


@pytest.mark.django_db
def test_exercise_3(api_client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)
    i = 5
    # Act
    response = api_client.get("/api/v1/courses/", {"id": course[i].id}, )
    # Assert
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == course[i].id


@pytest.mark.django_db
def test_exercise_4(api_client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)
    i = 5
    # Act
    response = api_client.get("/api/v1/courses/", {"name": course[i].name}, )
    # Assert
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == course[i].name


@pytest.mark.django_db
def test_exercise_5(api_client):
    # Arrange
    count = Course.objects.count()
    # Act
    response = api_client.post("/api/v1/courses/", {"id": "1", "name": "Hello Django", "students": {}})
    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_exercise_6(api_client, course_factory):
    # Arrange
    courses = course_factory(_quantity=100)
    # Act
    response = api_client.patch(f'/api/v1/courses/{courses[0].id}/', data={'name': 'Hello Django'})
    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    # Arrange
    courses = course_factory(_quantity=100)
    # Act
    response = api_client.delete(f'/api/v1/courses/{courses[0].id}/')
    # Assert
    assert response.status_code == 204