import requests


def test_foo(mock):
    # https://requests-mock.readthedocs.io/en/latest/matching.html
    mock.get("https://mysite.com", status_code=500, json={'message': 'Internal server error'})
    response = requests.get("https://mysite.com")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 500
    assert 'message' in response.json()
    assert response.json()['message'] == "Internal server error"
