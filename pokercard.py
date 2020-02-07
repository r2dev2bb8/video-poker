from card import Card

#===========================================================================
# Description: a poker card
#
# State Attributes
#   rank - string character 2 to 10 or A, J, Q, K
#   suit - string character ♥, ♦, ♠, ♣ (for heart, diamond, spade or club)
# Methods
#   getValue() - returns an integer from 2-14 depending on the rank of the card
#   __str__() - returns a string like '4♦' for 4 of diamonds
#   __int__() - equivalent of getValue() but can be called with int(instance)
#   __eq__() - compares if rank of cards is equal
#   __lt__() - compares if rank of one card is less than other
#===========================================================================

class PokerCard(Card):

    # change value of 1 to 14
    def getValue(self):
        old = super().getValue()
        return 14 if old == 1 else old

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank
