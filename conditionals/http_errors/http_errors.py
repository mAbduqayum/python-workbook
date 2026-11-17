status_code = int(input())

if 100 <= status_code <= 199:
    print("informational")
elif 200 <= status_code <= 299:
    print("success")
elif 300 <= status_code <= 399:
    print("redirection")
elif 400 <= status_code <= 499:
    print("client error")
elif 500 <= status_code <= 599:
    print("server error")
else:
    print("unknown status code")
