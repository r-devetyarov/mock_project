import requests

import requests_mock


def test_get_value_no_valid_param(mock):
    params = {"param": "no_valid_param"}
    mock.get(
        "https://ya.com/get_value?param=no_valid_param",
        status_code=400,
        json={"message": "Param must be valid"},
    )
    response = requests.get("https://ya.com/get_value", params)
    assert response.status_code == 400
    assert "message" in response.json()
    assert response.json()["message"] == "Param must be valid"


def test_get_value_valid_param(mock):
    params = {"param": "valid_param"}
    mock.get(
        "https://ya.com/get_value?param=valid_param",
        status_code=200,
        json={"message": "Success"},
    )
    response = requests.get("https://ya.com/get_value", params)
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Success"


def test_post_valid_body(mock):
    data = {"param_1": "valid", "param_2": "valid"}
    post_request(mock, data)

    response = requests.post("https://ya.com/post_value", json=data)
    assert response.status_code == 200
    assert "message" in response.json()
    assert response.json()["message"] == "Good, valid body"


def test_post_no_valid_body_param_1(mock):
    data = {"param_1": "no_valid", "param_2": "valid"}
    post_request(mock, data)
    response = requests.post("https://ya.com/post_value", json=data)
    assert response.status_code == 400
    assert "message" in response.json()
    assert response.json()["message"] == "Bad, no_valid body"


def test_post_no_valid_body_param_2(mock):
    data = {"param_1": "valid", "param_2": "no_valid"}
    post_request(mock, data)
    response = requests.post("https://ya.com/post_value", json=data)
    assert response.status_code == 400
    assert "message" in response.json()
    assert response.json()["message"] == "Bad, no_valid body"


def post_request(mock: requests_mock.Mocker(), data: dict) -> requests_mock.Mocker():
    if "valid" == data["param_1"] and "valid" == data["param_2"]:
        return mock.post(
            "https://ya.com/post_value",
            status_code=200,
            json={"message": "Good, valid body"},
        )
    else:
        return mock.post(
            "https://ya.com/post_value",
            status_code=400,
            json={"message": "Bad, no_valid body"},
        )
