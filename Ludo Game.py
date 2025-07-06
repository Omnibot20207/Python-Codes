import random

# ●  ┌  ─ ┐ │ └ ┘

"┌───────────┐"
"│           │"
"│           │"
"│           │"
"└───────────┘"

dice_art = {
    1: ("┌───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘"),

    2: ("┌───────────┐",
        "│  ●        │",
        "│           │",
        "│        ●  │",
        "└───────────┘"),

    3: ("┌───────────┐",
        "│  ●        │",
        "│     ●     │",
        "│        ●  │",
        "└───────────┘"),

    4: ("┌───────────┐",
        "│  ●     ●  │",
        "│           │",
        "│  ●     ●  │",
        "└───────────┘"),

    5: ("┌───────────┐",
        "│  ●     ●  │",
        "│     ●     │",
        "│  ●     ●  │",
        "└───────────┘"),

    6: ("┌───────────┐",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "│  ●     ●  │",
        "└───────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?:"))

is_running = True

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

#for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="" )
    print()

for die in dice:
    total += die
print(f"total: {total}")

answer = input("Do you Want to play again(Y/N):")
if not answer == "Y":
    is_running = False