from bybit.validators.response_validator import ResponseValidator


def test_valid_response():

    response = {
        "retCode": 0,
        "retMsg": "OK",
        "result": {},
    }

    ResponseValidator.validate(response)


def test_missing_retcode():

    response = {
        "retMsg": "OK",
        "result": {},
    }

    try:
        ResponseValidator.validate(response)
        assert False

    except ValueError as error:

        assert "retCode" in str(error)


def test_missing_retmsg():

    response = {
        "retCode": 0,
        "result": {},
    }

    try:
        ResponseValidator.validate(response)
        assert False

    except ValueError as error:

        assert "retMsg" in str(error)


def test_missing_result():

    response = {
        "retCode": 0,
        "retMsg": "OK",
    }

    try:
        ResponseValidator.validate(response)
        assert False

    except ValueError as error:

        assert "result" in str(error)


def test_invalid_type():

    try:

        ResponseValidator.validate([])

        assert False

    except ValueError as error:

        assert "dictionary" in str(error)