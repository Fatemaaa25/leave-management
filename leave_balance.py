def check_leave_balance(balance, requested):
    if requested <= 0 or requested > balance:
        return False
    return True