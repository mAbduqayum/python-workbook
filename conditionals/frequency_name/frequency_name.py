frequency = int(input())

if frequency < 3e9:
    print("radio waves")
elif frequency < 3e12:
    print("microwaves")
elif frequency < 4.3e14:
    print("infrared light")
elif frequency < 7.5e14:
    print("visible light")
elif frequency < 3e17:
    print("ultraviolet light")
elif frequency < 3e19:
    print("X-rays")
else:
    print("gamma rays")
