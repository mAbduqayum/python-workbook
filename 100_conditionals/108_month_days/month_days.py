month = input().lower()

match month:
    case "february":
        print("28 or 29")
    case "january" | "march" | "may" | "july" | "august" | "october" | "december":
        print("31")
    case "april" | "june" | "september" | "november":
        print("30")
    case _:
        print("Invalid month")