import itertools
import re
from copy import deepcopy
from collections import defaultdict
import time
with open('d7.txt', 'r') as f:
    data = f.read().split('\n')

print(data)

card_lookup = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
hands = []
for hand in data:
    cards = hand.split(" ")[0]
    bid = hand.split(" ")[1]
    cards = [x for x in cards]
    cards = [card_lookup[x] if x in card_lookup else int(x) for x in cards]
    hands.append((cards, bid))
    print(cards)

# compare hands by highest cards
def compare_hands(h1, h2):
    original_h1 = deepcopy(h1)
    original_h2 = deepcopy(h2)
    original_h1.sort()
    original_h2.sort()
    if original_h1 == h1 and original_h2 == h2:
        print("VERY VERY VERY SUS, LOOK FOR DEEP COPY ERRORS")
        print(h1, h2)
        with open("debug.txt", "a+") as f:
            f.write(str(h1) + "\n")
            f.write(str(h2) + "\n")
            f.write("\n")
        #time.sleep(1)
    print("CMP hands")
    print(h1, h2)
    for h1_card, h2_card in zip(h1, h2):
        print(h1_card, h2_card)
        if h1_card > h2_card:
            return 1
        elif h1_card < h2_card:
            return -1
    assert False

#assert compare_hands([13, 10, 1, 1, 10], [10, 5, 5, 1, 5]) == 1 
#assert compare_hands([2, 3, 4, 5, 6], [2, 3, 4, 5, 7]) == -1
#assert compare_hands([2, 3, 4, 5, 6], [3, 3, 4, 5, 6]) == -1
#assert compare_hands([11, 12, 12, 12, 14], [5, 5, 5, 10, 11]) == 1

# true or false if hand is five of a kind
def is_five_of_a_kind(cards):
    if cards.count(1) != 0:
        return False
    return len(set(cards)) == 1

assert is_five_of_a_kind([2, 2, 2, 2, 2]) == True

def is_four_of_a_kind(cards):
    if cards.count(1) != 0:
        return False
    cards = deepcopy(cards)
    cards.sort()
    return cards.count(cards[0]) == 4 or cards.count(cards[1]) == 4

assert is_four_of_a_kind([2, 2, 2, 2, 3]) == True
assert is_four_of_a_kind([2, 2, 2, 3, 3]) == False
assert is_four_of_a_kind([3, 2, 2, 2, 2]) == True

# looks good
def is_full_house(cards):
    if cards.count(1) != 0:
        return False
    cards = deepcopy(cards)
    cards.sort()
    if cards.count(cards[0]) == 3 and cards.count(cards[4]) == 2:
        return True
    elif cards.count(cards[0]) == 2 and cards.count(cards[4]) == 3:
        return True
    return False

assert is_full_house([2, 3, 2, 3, 2]) == True
assert is_full_house([2, 2, 2, 3, 3]) == True
assert is_full_house([2, 2, 2, 2, 3]) == False
assert is_full_house([2, 2, 4, 3, 3]) == False

def is_three_of_a_kind(cards):
    if cards.count(1) != 0:
        return False
    cards = deepcopy(cards)
    cards.sort()
    return cards.count(cards[0]) == 3 or cards.count(cards[1]) == 3 or cards.count(cards[2]) == 3

assert is_three_of_a_kind([2, 2, 2, 3, 4]) == True
assert is_three_of_a_kind([2, 2, 3, 3, 4]) == False
assert is_three_of_a_kind([2, 3, 3, 3, 4]) == True

def is_two_pairs(cards):
    if cards.count(1) != 0:
        return False
    cards = deepcopy(cards)
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
    if cards.count(1) != 0:
        return False
    cards = deepcopy(cards)
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

def find_if_hand_w_jokers(hand, func):
    originial_hand = deepcopy(hand) # just to be safe
    # loop from 14 to 2 and replace ALL jokers with that number
    if originial_hand.count(1) == 0:
        return False
    print("\n")
    print(func.__name__)
    # find all permutations of hands with jokers replaced, ie all pairs or triplets of numbers 2-14
    for elem in itertools.product(range(2, 15), repeat=originial_hand.count(1)):
        elem = list(elem)
        new_hand = [x if x != 1 else elem.pop(0) for x in originial_hand]
        assert len(elem) == 0
        if func(new_hand):
            return True
    return False

assert find_if_hand_w_jokers([13, 10, 1, 1, 10], is_four_of_a_kind) == True
assert find_if_hand_w_jokers([10, 5, 5, 1, 5], is_four_of_a_kind) == True
assert find_if_hand_w_jokers([12, 12, 12, 1, 14], is_four_of_a_kind) == True
assert find_if_hand_w_jokers([7, 1, 6, 1, 6], is_four_of_a_kind) == True
assert find_if_hand_w_jokers([1,4,4,4,1], is_five_of_a_kind) == True
assert find_if_hand_w_jokers([14,2,1,9,13], is_one_pair) == True
assert find_if_hand_w_jokers([1,1,1,8,1], is_five_of_a_kind) == True
assert find_if_hand_w_jokers([1,1,1,1,1], is_five_of_a_kind) == True

# return positive if h1 wins, negative if h2 wins and 0 if tie
def compare_hands_full(h1, h2):
    print(h1, h2)
    h1, h2 = h1[0], h2[0]
    if h1 == h2:
        print("TIE")
        exit()
        return 0
    for func in functions:
        if (func(h1) or find_if_hand_w_jokers(h1, func)) and not (func(h2) or find_if_hand_w_jokers(h2, func)):
            return 1
        elif (func(h2) or find_if_hand_w_jokers(h2, func)) and not (func(h1) or find_if_hand_w_jokers(h1, func)):
            return -1
        elif (func(h1) or find_if_hand_w_jokers(h1, func)) and (func(h2) or find_if_hand_w_jokers(h2, func)):
            print("TIE")
            break
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

# P2: 248777604 too low 
# 250310867 too high