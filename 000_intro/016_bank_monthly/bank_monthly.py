deposit = float(input("Enter initial deposit: "))
rate = float(input("Enter annual interest rate (%): "))
year1 = deposit * (1 + rate / 1200) ** 12
year2 = deposit * (1 + rate / 1200) ** 24
year3 = deposit * (1 + rate / 1200) ** 36
print(f"Balance after 1 year: {year1:.2f}")
print(f"Balance after 2 years: {year2:.2f}")
print(f"Balance after 3 years: {year3:.2f}")
