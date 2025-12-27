from src.validator import validate_password

def test_valid_password():
    # 8文字以上かつ数字あり -> Trueになるはず
    assert validate_password("pass1234") is True

def test_short_password():
    # 短すぎる -> Falseになるはず
    assert validate_password("12345") is False

def test_no_digit_password():
    # 数字がない -> Falseになるはず
    assert validate_password("password") is False
