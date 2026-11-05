from leave_balance import check_leave_balance


def test_valid():
    assert check_leave_balance(10, 4) is True

def test_insufficient():
    assert check_leave_balance(2, 5) is False


def test_zero():
    assert check_leave_balance(10, 0) is False


def test_invalid_negative():
    assert check_leave_balance(10, -1) is False