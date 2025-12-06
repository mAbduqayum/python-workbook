bill = float(input("Enter bill amount: "))
tip_percent = int(input("Enter tip percentage: "))
tip_amount = bill * tip_percent / 100
total = bill + tip_amount
print(f"Tip amount: {tip_amount:.2f}")
print(f"Total amount: {total:.2f}")
