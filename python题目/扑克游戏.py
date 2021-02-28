import random


class Card(object):

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = "A"
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return "%s%s" % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()


class Poker(object):
    def __init__(self):
        self._cards = [
            Card(suite, face)
            for suite in '♠♣♥■'
            for face in range(1, 14)
        ]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        return self._current < len(self._cards)


class Player(object):

    def __init__(self, name):
        self._name = name
        self.cards_on_card = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_card(self):
        return self.cards_on_card

    def get(self, card):
        self.cards_on_card.append(card)

    def arrange(self, card_key):
        self.cards_on_card.sort(key=card_key)

    @cards_on_card.setter
    def cards_on_card(self, value):
        self.cards_on_card = value


def get_key(fcard):
    return fcard.suite, fcard.face


if __name__ == '__main__':
    p = Poker()
    p.shuffle()
