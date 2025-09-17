# Note to Frequency

Write a program that reads the name of a musical note from the user and displays the note's frequency. This exercise starts with basic notes and can be extended to support multiple octaves.

## Task
**Basic Version:**
- Read the name of a note from the user (C4, D4, E4, F4, G4, A4, B4)
- Display the note's frequency

**Extended Version (Optional Challenge):**
- Support all notes from C0 to C8
- Use the mathematical relationship between octaves

## Basic Note Frequencies (4th Octave)
| Note | Frequency (Hz) |
|------|----------------|
| C4 | 261.63 |
| D4 | 293.66 |
| E4 | 329.63 |
| F4 | 349.23 |
| G4 | 392.00 |
| A4 | 440.00 |
| B4 | 493.88 |

## Examples
**Example 1 (Basic):**
```
C4
261.63
```

**Example 2 (Basic):**
```
A4
440.00
```

**Example 3 (Extended):**
```
C3
130.82
```

**Example 4 (Extended):**
```
A5
880.00
```

**Example 5 (Invalid):**
```
X4
Invalid note
```

## Mathematical Relationship (For Extended Version)
- The frequency of any note in octave n is half the frequency of the corresponding note in octave n + 1
- To calculate: frequency = base_frequency / (2^(4-octave_number))
- Where base_frequency is the frequency of the note in the 4th octave

