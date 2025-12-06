decibel = int(input())

if decibel < 40:
    print("Quieter than Quiet Room")
elif decibel == 40:
    print("Quiet Room")
elif decibel < 70:
    print("Between Quiet Room and Alarm Clock")
elif decibel == 70:
    print("Alarm Clock")
elif decibel < 106:
    print("Between Alarm Clock and Gas Lawnmower")
elif decibel == 106:
    print("Gas Lawnmower")
elif decibel < 130:
    print("Between Gas Lawnmower and Jackhammer")
elif decibel == 130:
    print("Jackhammer")
else:
    print("Louder than Jackhammer")
