import random


def create_deck() -> list[str]:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['H', 'D', 'C', 'S']
    return [rank + suit for suit in suits for rank in ranks]


def shuffle_deck(deck: list[str]) -> list[str]:
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled


if __name__ == "__main__":
    # Test your functions
    deck = create_deck()
    print(f"Deck size: {len(deck)}")  # 52
    print(f"First 5 cards: {deck[:5]}")

    shuffled = shuffle_deck(deck)
    print(f"Shuffled first 5: {shuffled[:5]}")
