import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.cardgame = CardGame()
        self.card1 = Card("club", 1)
        self.card2 = Card("heart", 8)
        self.card3 = Card("diamond", 11)
        self.cards = [self.card1, self.card2, self.card3]
            
    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    def test_check_for_not_ace(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card2))

    def test_check_for_higher(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card1, self.card2))

    def test_card_total(self):
        self.assertEqual("You have a total of 20", self.cardgame.cards_total(self.cards))
