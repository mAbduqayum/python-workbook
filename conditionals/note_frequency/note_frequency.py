note = input()

if len(note) == 2:
    note_name, octave_char = note
    note_name = note_name.upper()  # Convert to uppercase for consistency

    if note_name == "C" and octave_char in "012345678":
        base_freq = 261.63
    elif note_name == "D" and octave_char in "012345678":
        base_freq = 293.66
    elif note_name == "E" and octave_char in "012345678":
        base_freq = 329.63
    elif note_name == "F" and octave_char in "012345678":
        base_freq = 349.23
    elif note_name == "G" and octave_char in "012345678":
        base_freq = 392.00
    elif note_name == "A" and octave_char in "012345678":
        base_freq = 440.00
    elif note_name == "B" and octave_char in "012345678":
        base_freq = 493.88
    else:
        print("Invalid note")
        base_freq = None

    if base_freq is not None:
        octave = int(octave_char)
        octave_diff = 4 - octave
        if octave_diff == 0:
            frequency = base_freq
        elif octave_diff > 0:
            frequency = base_freq / (2**octave_diff)
        else:
            frequency = base_freq * (2 ** (-octave_diff))

        frequency_str = f"{frequency:.2f}"
        print(frequency_str)
else:
    print("Invalid note")
