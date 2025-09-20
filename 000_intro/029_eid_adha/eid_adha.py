year = int(input("Enter Gregorian year: "))
hijri_year = (year - 622) * 1.030684
eid_day = int((hijri_year - int(hijri_year)) * 354 + 10)
if eid_day > 30:
    eid_day -= 30
    eid_month = 7
else:
    eid_month = 6
print(f"Estimated Eid al-Adha: {eid_month} {eid_day}, {year}")
