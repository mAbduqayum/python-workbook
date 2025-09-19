note = input()

if len(note) == 2:
    note = note.upper()
    note_name, octave_char = note

    base_freq = None

    if not octave_char.isdigit():
        print("Invalid note")
    elif note_name == 'C':
        base_freq = 261.63
    elif note_name == 'D':
        base_freq = 293.66
    elif note_name == 'E':
        base_freq = 329.63
    elif note_name == 'F':
        base_freq = 349.23
    elif note_name == 'G':
        base_freq = 392.00
    elif note_name == 'A':
        base_freq = 440.00
    elif note_name == 'B':
        base_freq = 493.88

    if base_freq is not None:
        octave = int(octave_char)
        frequency = base_freq * (2 ** (octave - 4))
        print(f"{frequency:.2f}")
else:
    print("Invalid note")