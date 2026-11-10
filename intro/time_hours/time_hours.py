total_hours = float(input())
total_minutes = round(total_hours * 60)
days = total_minutes // (24 * 60)
remaining_hours = total_minutes // 60 % 24
minutes = total_minutes % 60
print(days, remaining_hours, minutes)
