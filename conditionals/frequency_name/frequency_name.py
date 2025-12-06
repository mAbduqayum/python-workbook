frequency = int(input())

if frequency < 3e9:
    print("Radio Waves")
elif frequency < 3e12:
    print("Microwaves")
elif frequency < 4.3e14:
    print("Infrared Light")
elif frequency < 7.5e14:
    print("Visible Light")
elif frequency < 3e17:
    print("Ultraviolet Light")
elif frequency < 3e19:
    print("X-Rays")
else:
    print("Gamma Rays")
