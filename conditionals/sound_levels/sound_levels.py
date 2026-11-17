decibel = int(input())

if decibel < 40:
    print("quieter than quiet room")
elif decibel == 40:
    print("quiet room")
elif decibel < 70:
    print("between quiet room and alarm clock")
elif decibel == 70:
    print("alarm clock")
elif decibel < 106:
    print("between alarm clock and gas lawnmower")
elif decibel == 106:
    print("gas lawnmower")
elif decibel < 130:
    print("between gas lawnmower and jackhammer")
elif decibel == 130:
    print("jackhammer")
else:
    print("louder than jackhammer")
