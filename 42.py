import random

dice_faces = {
    1: [
        "╔═════╗",
        "║     ║",
        "║  ●  ║",
        "║     ║",
        "╚═════╝"
    ],
    2: [
        "╔═════╗",
        "║ ●   ║",
        "║     ║",
        "║   ● ║",
        "╚═════╝"
    ],
    3: [
        "╔═════╗",
        "║ ●   ║",
        "║  ●  ║",
        "║   ● ║",
        "╚═════╝"
    ],
    4: [
        "╔═════╗",
        "║ ● ● ║",
        "║     ║",
        "║ ● ● ║",
        "╚═════╝"
    ],
    5: [
        "╔═════╗",
        "║ ● ● ║",
        "║  ●  ║",
        "║ ● ● ║",
        "╚═════╝"
    ],
    6: [
        "╔═════╗",
        "║ ● ● ║",
        "║ ● ● ║",
        "║ ● ● ║",
        "╚═════╝"
    ]
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))
    for line in dice_faces.get(dice[die]):
        print(line)
# for item in dice:
#     for die in dice_faces.get(item):
#         print(die)

for die in dice:
    total += die 

print(total)