note = input()

if len(note) == 2 and note[1] in "012345678":
    note_name, octave_char = note
    note_name = note_name.upper()

    if note_name == "C":
        base_freq = 261.63
    elif note_name == "D":
        base_freq = 293.66
    elif note_name == "E":
        base_freq = 329.63
    elif note_name == "F":
        base_freq = 349.23
    elif note_name == "G":
        base_freq = 392.00
    elif note_name == "A":
        base_freq = 440.00
    elif note_name == "B":
        base_freq = 493.88
    else:
        print("Invalid note")
        base_freq = None

    if base_freq is not None:
        octave = int(octave_char)
        # Each octave up doubles the frequency; the base frequencies are octave 4
        frequency = base_freq * 2 ** (octave - 4)
        print(f"{frequency:.2f}")
else:
    print("Invalid note")
