def request_leave(balance, days):
    if days <= 0:
        return "Invalid leave request"
    if days > balance:
        return "Insufficient leave balance"
    return "Leave approved"


if __name__ == "__main__":
    balance = int(input("Enter leave balance: "))
    days = int(input("Enter leave days requested: "))
    print(request_leave(balance, days))
