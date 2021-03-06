from typing import List

from cards.card import Deck, GameCard


class Player:
    hand: List[GameCard]
    id : int

    def __init__(self, hand, id):
        self.hand = hand
        self.id = id

    def draw(self) -> GameCard:
        return self.hand.pop(0)

    def out_of_cards(self) -> bool:
        return len(self.hand) == 0

    def take(self, card: GameCard):
        self.hand.append(card)


class War:
    deck: Deck
    player_one: Player
    player_two: Player

    def __init__(self, deck: Deck):
        self.deck = deck

    def setup_game(self):
        deck_one, deck_two = self.deck.split_deck()
        self.deck.cards.clear()
        self.player_one = Player(deck_one)
        self.player_two = Player(deck_two)

    def draw(self):
        p1_card = self.player_one.draw()
        print("Player 1 draws card {}".format(p1_card))
        p2_card = self.player_two.draw()
        print("Player 2 draws card {}".format(p2_card))
        self.deck.cards += [p1_card, p2_card]
        winner: Player
        if p1_card > p2_card:
            winner = self.player_one
        elif p1_card < p2_card:
            winner = self.player_two
        else:
            print("Equal!")
            pass
        if winner:
            print("{} wins".format(winner))
            for card in self.deck.cards:
                winner.take(card)
            self.deck.cards.clear()
