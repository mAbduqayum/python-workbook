status_code = int(input())

if 100 <= status_code <= 199:
    print("Informational")
elif 200 <= status_code <= 299:
    print("Success")
elif 300 <= status_code <= 399:
    print("Redirection")
elif 400 <= status_code <= 499:
    print("Client Error")
elif 500 <= status_code <= 599:
    print("Server Error")
else:
    print("Unknown status code")