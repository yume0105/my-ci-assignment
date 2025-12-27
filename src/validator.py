def validate_password(password: str) -> bool:
    """
    パスワードの強度を判定する関数
    条件: 8文字以上 かつ 数字が含まれていること
    """
    if len(password) < 8:
        return False
    
    # 数字が含まれているかチェック
    has_digit = any(char.isdigit() for char in password)
    
    return has_digit
