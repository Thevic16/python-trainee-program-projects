from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    '''
    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)
    '''


if __name__ == '__main__':
    # DataClassCard
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    print(queen_of_hearts.rank)
    print(queen_of_hearts)
    print(queen_of_hearts == DataClassCard('Q', 'Hearts'))

    # RegularCard
    queen_of_hearts = RegularCard('Q', 'Hearts')
    print(queen_of_hearts.rank)
    print(queen_of_hearts)
    print(queen_of_hearts == RegularCard('Q', 'Hearts'))
