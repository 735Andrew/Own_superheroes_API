import pytest
import requests as r


@pytest.fixture
def add_hero_correct_URL():
    return "http://127.0.0.1:5000/hero"


def test_correct_hero_add(add_hero_correct_URL):
    data = {"name": "thor"}
    response = r.post(add_hero_correct_URL, json=data)

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "intelligence": 100,
        "name": "thor",
        "power": 68,
        "speed": 25,
        "strength": 53,
    }


def test_duplication_in_hero_add(add_hero_correct_URL):
    data = {"name": "thor"}
    response = r.post(add_hero_correct_URL, json=data)

    assert response.status_code == 409
    assert response.json() == {
        "error": "character with given name have been already added."
    }


def test_unknown_hero_in_hero_add(add_hero_correct_URL):
    data = {"name": "super-thor"}
    response = r.post(add_hero_correct_URL, json=data)

    assert response.status_code == 404
    assert response.json() == {"error": "character with given name not found"}


def test_correct_hero_explore_1():
    URL = "http://127.0.0.1:5000/hero?name=thor&strength=75"
    response = r.get(URL)

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "intelligence": 100,
        "name": "thor",
        "power": 68,
        "speed": 25,
        "strength": 53,
    }


def test_correct_hero_explore_2():
    URL = "http://127.0.0.1:5000/hero?intelligence=10&power=50"
    response = r.get(URL)

    assert response.status_code == 200
    assert response.json() == {
        "intelligence": {
            "Heroes with an ability level 10": [],
            "Heroes with an ability level higher than 10": [
                {
                    "id": 1,
                    "intelligence": 100,
                    "name": "thor",
                    "power": 68,
                    "speed": 25,
                    "strength": 53,
                }
            ],
            "Heroes with an ability level lower than 10": [],
        },
        "power": {
            "Heroes with an ability level 50": [],
            "Heroes with an ability level higher than 50": [
                {
                    "id": 1,
                    "intelligence": 100,
                    "name": "thor",
                    "power": 68,
                    "speed": 25,
                    "strength": 53,
                }
            ],
            "Heroes with an ability level lower than 50": [],
        },
    }


def test_incorrect_hero_explore():
    URL = "http://127.0.0.1:5000/hero?pants_color=purple"
    response = r.get(URL)

    assert response.status_code == 422
    assert response.json() == {"error": f"argument 'pants_color' is not supported."}
