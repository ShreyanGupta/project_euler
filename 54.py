def create_hand(card):
    try:
        return int(card[0]), card[1]
    except ValueError:
        d = dict({'T':10, 'J':11, 'Q':12, 'K':13, 'A':14})
        return d[card[0]], card[1]


def parse(l):
    cards = l.split()
    cards = list(map(create_hand, cards))
    p1 = sorted(cards[0:5])
    p2 = sorted(cards[5:10])
    return p1, p2


def is_straight_flush(hand):
    straight = is_straight(hand)
    flush = is_flush(hand)
    if straight and flush:
        return (8, straight[1])
    return None


def is_four_of_a_kind(hand):
    if hand[0][0] == hand[1][0] and hand[0][0] == hand[2][0] and hand[0][0] == hand[3][0]:
        return (7, hand[0][0])
    if hand[4][0] == hand[1][0] and hand[4][0] == hand[2][0] and hand[4][0] == hand[3][0]:
        return (7, hand[4][0])
    return None


def is_full_house(hand):
    # 00011, 00111
    if hand[0][0] == hand[1][0] or hand[3][0] == hand[4][0]:
        return None
    if hand[2][0] == hand[0][0]:
        return (6, 20 * hand[0][0] + hand[4][0])
    if hand[2][0] == hand[4][0]:
        return (6, 20 * hand[4][0] + hand[0][0])
    return None


def is_flush(hand):
    for card in hand:
        if card[1] != hand[0][1]:
            return None
    return (5, 0)


def is_straight(hand):
    for i in range(1, 5):
        if hand[i][0] != hand[0][0] + i and hand[i][0] != hand[0][0] + i + 8:
            return None
    return (4, hand[0][0])


def is_three_of_a_kind(hand):
    # 00012, 01112 01222
    for i in [0, 1, 2]:
        if hand[i][0] == hand[i+1][0] and hand[i][0] == hand[i+2][0]:
            return (3, hand[i][0])
    return None


def is_two_pair(hand):
    # 00112 00122 01122
    for i,j in [(0,2), (0,3), (1,3)]:
        if hand[i][0] == hand[i+1][0] and hand[j][0] == hand[j+1][0]:
            return (2, 20 * hand[j][0] + hand[i][0])
    return None


def is_pair(hand):
    # 00123 01123 01223 01233
    for i in range(4):
        if hand[i][0] == hand[i+1][0]:
            return (1, hand[i][0])
    return False


def high_card(hand):
    return (0, hand[4][0])


def rank(hand):
    return is_straight_flush(hand) or is_four_of_a_kind(hand) or is_full_house(hand) \
        or is_flush(hand) or is_straight(hand) or is_three_of_a_kind(hand) \
        or is_two_pair(hand) or is_pair(hand) or high_card(hand)


p1_win = 0
with open("poker.txt") as f:
    for line in f:
        p1, p2 = parse(line)
        print(rank(p1), "::::", p1)
        print(rank(p2), "::::", p2)
        p1_win += (rank(p1) > rank(p2))

print("P1 win", p1_win)

# print(is_straight([(2,2), (3,2), (4,2), (5,2), (14,2)]))
# print(is_straight([(2,2), (3,2), (4,2), (5,2), (6,2)]))
# print(is_straight([(2,2), (3,2), (4,2), (5,2), (7,2)]))