import itertools
import re
from collections import defaultdict
with open('d7.txt', 'r') as f:
    data = f.read().split('\n')

print(data)

card_lookup = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
hands = []
for hand in data:
    cards = hand.split(" ")[0]
    bid = hand.split(" ")[1]
    cards = [x for x in cards]
    cards = [card_lookup[x] if x in card_lookup else int(x) for x in cards]
    cards.sort()
    hands.append((cards, bid))
    print(cards)

# compare hands by highest cards
def compare_hands(h1, h2):
    h1.sort()
    h2.sort()
    for h1_card, h2_card in zip(reversed(h1), reversed(h2)):
        if h1_card > h2_card:
            return 1
        elif h1_card < h2_card:
            return -1
    assert False

assert compare_hands([2, 3, 4, 5, 6], [2, 3, 4, 5, 7]) == -1
assert compare_hands([11, 12, 12, 12, 14], [5, 5, 5, 10, 11]) == 1

# true or false if hand is five of a kind
def is_five_of_a_kind(cards):
    return len(set(cards)) == 1

assert is_five_of_a_kind([2, 2, 2, 2, 2]) == True

def is_four_of_a_kind(cards):
    cards.sort()
    return cards.count(cards[0]) == 4 or cards.count(cards[1]) == 4

assert is_four_of_a_kind([2, 2, 2, 2, 3]) == True
assert is_four_of_a_kind([2, 2, 2, 3, 3]) == False
assert is_four_of_a_kind([3, 2, 2, 2, 2]) == True

def is_full_house(cards):
    cards.sort()
    return cards.count(cards[0]) == 3 and cards.count(cards[4]) == 2 or cards.count(cards[0]) == 2 and cards.count(cards[4]) == 3

assert is_full_house([2, 2, 2, 3, 3]) == True
assert is_full_house([2, 2, 2, 2, 3]) == False
assert is_full_house([2, 2, 4, 3, 3]) == False

def is_three_of_a_kind(cards):
    cards.sort()
    return cards.count(cards[0]) == 3 or cards.count(cards[1]) == 3 or cards.count(cards[2]) == 3

assert is_three_of_a_kind([2, 2, 2, 3, 4]) == True
assert is_three_of_a_kind([2, 2, 3, 3, 4]) == False
assert is_three_of_a_kind([2, 3, 3, 3, 4]) == True

def is_two_pairs(cards):
    cards.sort()
    # get counts of each character in cards
    counts = defaultdict(int)
    for card in cards:
        counts[card] += 1
    # check if there are two pairs
    pairs = 0
    for card in counts:
        if counts[card] == 2:
            pairs += 1
    return pairs == 2

assert is_two_pairs([2, 2, 3, 3, 4]) == True
assert is_two_pairs([2, 2, 2, 3, 4]) == False
assert is_two_pairs([2, 2, 3, 4, 4]) == True

def is_one_pair(cards):
    cards.sort()
    # get counts of each character in cards
    counts = defaultdict(int)
    for card in cards:
        counts[card] += 1
    # check if there are two pairs
    pairs = 0
    for card in counts:
        if counts[card] == 2:
            pairs += 1
    return pairs == 1

assert is_one_pair([2, 2, 3, 4, 5]) == True
assert is_one_pair([2, 2, 2, 3, 4]) == False

functions = [is_five_of_a_kind, is_four_of_a_kind, is_full_house, is_three_of_a_kind, is_two_pairs, is_one_pair]

# return positive if h1 wins, negative if h2 wins and 0 if tie
def compare_hands_full(h1, h2):
    print(h1, h2)
    h1, h2 = h1[0], h2[0]
    if h1 == h2:
        return 0
    for func in functions:
        if func(h1) and not func(h2):
            return 1
        elif func(h2) and not func(h1):
            return -1
    return compare_hands(h1, h2)

# use custom sort to sort hands
import functools
hands.sort(key=functools.cmp_to_key(compare_hands_full))
print(hands)
hands = [(x[0], int(x[1])) for x in hands]
print(hands)
ans = 0
for idx, hand in enumerate(hands):
    ans += hand[1] * (idx + 1)
print(ans)
# 248564955 too high
# 247742088
# 182172106 low? 