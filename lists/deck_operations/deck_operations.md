# Deck Operations

Create and shuffle a deck of playing cards.

## Task

- Create a function `create_deck()` that generates a standard 52-card deck
- Create a function `shuffle_deck(deck)` that shuffles the deck
- Cards can be represented as strings like "2H" (2 of Hearts), "AK" (Ace of Spades)

## Template:

```python
def create_deck() -> list[str]:
    pass


def shuffle_deck(deck: list[str]) -> list[str]:
    pass


if __name__ == "__main__":
    # Test your functions
    deck = create_deck()
    print(f"Deck size: {len(deck)}")  # 52
    print(f"First 5 cards: {deck[:5]}")

    shuffled = shuffle_deck(deck)
    print(f"Shuffled first 5: {shuffled[:5]}")
```

<details>
<summary><strong>Hint</strong></summary>

- **create_deck():**
    - Ranks: 2-10, J, Q, K, A (or use strings/numbers)
    - Suits: H (Hearts), D (Diamonds), C (Clubs), S (Spades)
    - Use nested loops or list comprehension to combine ranks and suits
- **shuffle_deck():**
    - Import `random` module
    - Create a copy of the deck
    - Use `random.shuffle()` to shuffle in place, or
    - Use `random.sample(deck, len(deck))` to create a shuffled copy

</details>

## Note

- Standard deck has 52 cards (13 ranks × 4 suits)
- shuffle_deck should return a new shuffled deck (not modify original)
- Card representation can vary (e.g., "2H", "2♥", or tuples)

<details>
<summary><strong>Historical Note</strong></summary>

Playing cards were invented in China during the Tang dynasty (9th century), likely evolving from earlier paper-based games. They spread westward through the Islamic world, reaching Europe by the 14th century where the modern four-suit system developed. The Fisher-Yates shuffle algorithm, the mathematically optimal shuffling method, was published by statisticians Ronald Fisher and Frank Yates in 1938 for manual card shuffling. In 1964, Richard Durstenfeld adapted it for computers, creating an efficient in-place version. The algorithm guarantees every permutation has equal probability—a property many intuitive shuffling methods surprisingly lack.

</details>
