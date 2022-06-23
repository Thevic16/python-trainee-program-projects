from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'


RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f'{self.__class__.__name__}({cards})'


if __name__ == '__main__':
    print(Deck())

    ace_of_spades = PlayingCard('A', '♠')
    print(ace_of_spades)

    # Comparing Cards
    queen_of_hearts = PlayingCard('Q', '♡')
    print(queen_of_hearts.sort_index)
    ace_of_spades = PlayingCard('A', '♠')
    print(ace_of_spades.sort_index)
    print(ace_of_spades > queen_of_hearts)
