total_hours = float(input())
days = int(total_hours // 24)
remaining_hours = int(total_hours % 24)
minutes = int((total_hours * 60) % 60)
print(
    f"{total_hours} hours = {days} days, {remaining_hours} hours, and {minutes} minutes"
)
