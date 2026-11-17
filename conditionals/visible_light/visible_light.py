wavelength = int(input())

if 380 <= wavelength < 450:
    print("violet")
elif 450 <= wavelength < 495:
    print("blue")
elif 495 <= wavelength < 570:
    print("green")
elif 570 <= wavelength < 590:
    print("yellow")
elif 590 <= wavelength < 620:
    print("orange")
elif 620 <= wavelength <= 750:
    print("red")
else:
    print("outside visible spectrum")
