# Cards

def point(x):
    return {
        'J': 1,
        'Q': 2,
        'K': 3,
        'A': 4
    }.get(x, 0)


def points(hand):
    rank = [i[0] for i in hand]
    suit = [i[1] for i in hand]
    pt = sum([point(i) for i in rank])
    suit_list = ['C', 'D', 'H', 'S']
    for s in suit_list:
        if suit.count(s) == 0:
            pt += 3
        elif suit.count(s) == 1:
            pt += 2
        elif suit.count(s) == 2:
            pt += 1
    return pt


# myhand = ['AH', 'TH', 'QH', '5D', '8H', '6H']
# print("Your Point is %d " % points(myhand))
