initial = input().lower()
final = input().lower()

if initial == final:
    print("No transition")
elif initial == "solid" and final == "liquid":
    print("melting")
elif initial == "solid" and final == "gas":
    print("sublimation")
elif initial == "liquid" and final == "solid":
    print("freezing")
elif initial == "liquid" and final == "gas":
    print("vaporization")
elif initial == "gas" and final == "liquid":
    print("condensation")
elif initial == "gas" and final == "solid":
    print("deposition")
