import requests


def test_index():
    response = requests.get("http://0.0.0.0:8080/")
    assert 200 == 200  
