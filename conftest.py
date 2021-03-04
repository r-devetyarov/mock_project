import pytest
import requests_mock


@pytest.fixture
def mock():
    with requests_mock.Mocker() as mock_instance:
        yield mock_instance
