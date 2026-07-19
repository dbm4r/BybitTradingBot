from unittest.mock import Mock, patch

from bybit.http.http_client import HttpClient


@patch("requests.request")
def test_send_get_request(mock_request):

    response = Mock()

    response.raise_for_status.return_value = None

    response.json.return_value = {
        "retCode": 0,
        "result": {},
    }

    mock_request.return_value = response

    client = HttpClient()

    result = client.send(
        method="GET",
        url="https://test.com",
    )

    assert result["retCode"] == 0

    mock_request.assert_called_once()


@patch("requests.request")
def test_send_with_params(mock_request):

    response = Mock()

    response.raise_for_status.return_value = None

    response.json.return_value = {
        "retCode": 0,
    }

    mock_request.return_value = response

    client = HttpClient()

    client.send(
        method="GET",
        url="https://test.com",
        params={
            "symbol": "BTCUSDT",
        },
    )

    _, kwargs = mock_request.call_args

    assert kwargs["params"]["symbol"] == "BTCUSDT"


@patch("requests.request")
def test_send_with_body(mock_request):

    response = Mock()

    response.raise_for_status.return_value = None

    response.json.return_value = {
        "retCode": 0,
    }

    mock_request.return_value = response

    client = HttpClient()

    client.send(
        method="POST",
        url="https://test.com",
        body={
            "symbol": "BTCUSDT",
        },
    )

    _, kwargs = mock_request.call_args

    assert "BTCUSDT" in kwargs["data"]


@patch("requests.request")
def test_send_uses_timeout(mock_request):

    response = Mock()

    response.raise_for_status.return_value = None

    response.json.return_value = {
        "retCode": 0,
    }

    mock_request.return_value = response

    client = HttpClient()

    client.send(
        method="GET",
        url="https://test.com",
    )

    _, kwargs = mock_request.call_args

    assert kwargs["timeout"] == (
        5,
        30,
    )


@patch("requests.request")
def test_raise_for_status_called(mock_request):

    response = Mock()

    response.raise_for_status.return_value = None

    response.json.return_value = {
        "retCode": 0,
    }

    mock_request.return_value = response

    client = HttpClient()

    client.send(
        method="GET",
        url="https://test.com",
    )

    response.raise_for_status.assert_called_once()


@patch("requests.request")
def test_json_called(mock_request):

    response = Mock()

    response.raise_for_status.return_value = None

    response.json.return_value = {
        "retCode": 0,
    }

    mock_request.return_value = response

    client = HttpClient()

    client.send(
        method="GET",
        url="https://test.com",
    )

    response.json.assert_called_once()