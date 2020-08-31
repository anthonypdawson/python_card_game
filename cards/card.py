from dataclasses import dataclass, field
from random import sample
from typing import List, Tuple

RANKS = [str(i) for i in range(2, 10)] + ['J', 'Q', 'K', 'A']
SUITS = ['C', 'D', 'H', 'S']


@dataclass(order=True)
class GameCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'


def make_deck():
    return [GameCard(r, s) for r in RANKS for s in SUITS]


@dataclass
class Deck:
    cards: List[GameCard] = field(default_factory=make_deck)

    def split_deck(self) -> Tuple:
        first_deck = sample(self.cards, k=26)
        second_deck = [c for c in self.cards if c not in first_deck]
        return first_deck, second_deck
