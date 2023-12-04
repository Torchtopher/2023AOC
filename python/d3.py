from collections import defaultdict
with open("d3.txt", "r") as f:
    data = f.read().strip().split("\n")

print(data)
ans = 0

card_lookup = {} # card number -> number of winning numbers
for idx, card in enumerate(data):
    print(card)
    our_nums = card.split("|")[0].split(":")[1].strip().split(" ")
    print(our_nums)
    win_nums = card.split("|")[1].strip().split(" ")
    # remove any empty strings
    win_nums = list(filter(None, win_nums))
    our_nums = list(filter(None, our_nums))
    print(win_nums)
    our_nums_set = set(our_nums)
    win_nums_set = set(win_nums)
    intersection = our_nums_set.intersection(win_nums_set)
    card_lookup[idx + 1] = len(intersection)
    print(intersection)
    if len(intersection) == 0:
        continue
    score = 1
    for i in range(len(intersection) - 1):
        score *= 2
    print(f"Score: {score} for card {idx}") 
    ans += score

print(ans)

p2 = 0
occurance_dict = defaultdict(int)
memo = {}
def calc_cards_recursive(idx_start_card):   
    occurance_dict[idx_start_card] += 1
    num_wins = card_lookup[idx_start_card]
    #print(f"Card {idx_start_card} has {num_wins} winning numbers")
    if num_wins == 0:
        return 
    for i in range(1, num_wins + 1):
        calc_cards_recursive(idx_start_card + i)
    return
print(card_lookup)

for i in range(1, len(card_lookup) + 1):
    calc_cards_recursive(i)

print(occurance_dict)
for key, val in occurance_dict.items():
    p2 += val

print(p2)
