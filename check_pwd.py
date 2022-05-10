def check_pwd(test_string):
    if len(test_string) < 8 or len(test_string) > 20:
        return False
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    for letter in test_string:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            has_lower = True
        if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            has_upper = True
        if letter in '0123456789':
            has_digit = True
        if letter in '~`!@#$%^&*()_+-=':
            has_symbol = True
    if not has_lower or not has_upper or not has_digit or not has_symbol:
        return False
    return True


if __name__ == '__main__':
    check_pwd(')^xqJpfV!~POb')
