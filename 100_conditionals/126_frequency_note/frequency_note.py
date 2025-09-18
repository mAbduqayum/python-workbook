frequency = float(input())

# Check if frequency is within ±1 Hz of any note
if abs(frequency - 261.63) <= 1.0:
    print("C4")
elif abs(frequency - 293.66) <= 1.0:
    print("D4")
elif abs(frequency - 329.63) <= 1.0:
    print("E4")
elif abs(frequency - 349.23) <= 1.0:
    print("F4")
elif abs(frequency - 392.00) <= 1.0:
    print("G4")
elif abs(frequency - 440.00) <= 1.0:
    print("A4")
elif abs(frequency - 493.88) <= 1.0:
    print("B4")
else:
    print("No match")