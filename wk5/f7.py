"""
Small blackjack game
"""
import random
cards = {}

for num in range(2, 11):
    cards[str(num)] = num
cards["ACE-11"] = 11
cards["ACE-1"] = 1

for face_card in list("KQJ"):
    cards[face_card] = 10

suits = "Hearts,Diamonds,Spades,Clubs".split(",")
#print(suits)

total = 0
turns = []
for i in range(2): # running loop twice
    random_card_key = random.choice(list(cards.keys()))
    random_suit = random.choice(suits)
    #print(random_card_key)
    total += cards[random_card_key]
    turns.append(f"You received a {random_card_key} of {random_suit}")

for turn in turns:
    print(turn)
print("Your total is", total)
# print(turn, total)
while total <= 21:
    decision = input("Do you want to (H)it or (S)tay? ").upper()[0]
    if decision == "S":
        break
    random_card_key = random.choice(list(cards))
    random_suit = random.choice(suits)
    total += cards[random_card_key]
    turns.append(f"You received a {random_card_key} of {random_suit}")
    print(turns[-1])
    print("Your total is", total)

if total <= 21:
    print("You won because you didn't go over 21")
else:
    print("Sorry, but you went over 21")
