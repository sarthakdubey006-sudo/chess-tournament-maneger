import random
import time
import questionary
print("Welcome to the Chess Tournamnet Manager created by Sarthak Dubey.")
time.sleep(2)



player = []

i = 1
while i<= 4:
    
    name = input(f"Enter player {i} name: ")

    if i == 1:
        p1 = name
    elif i ==2:
        p2 = name
    elif i == 3:
        p3 = name
    elif i ==4:
        p4 = name
    i += 1


player.append(p1)
player.append(p2)
player.append(p3)
player.append(p4)

print(f"Players playing the tournament are {player}")
time.sleep(1)

print("Creating Tournament Fixture.....")
time.sleep(2)
print("First Round!")
time.sleep(1)
random.shuffle(player)


print(f"Match 1 is {player[0]} v/s {player[1]}")
time.sleep(1)
print(f"Match 2 is {player[2]} v/s {player[3]}")
time.sleep(1)
print(f"MATCH 1 : THE OG {player[0]} v/s THE GOAT {player[1]}")
time.sleep(1)
print("match in progresss..........")
time.sleep(5)

w1 = questionary.select(
    "who won?",
    choices=[
        player[0],
        player[1],
        "Draw",
    ]
).ask()

if w1 == "Draw":
    print(f"Time for rematch... {player[0]} v/s {player[1]}")
    w1 = questionary.select(
    "who won?",
    choices=[
        player[0],
        player[1],
    ]
).ask()
else:
    print(f"THE WINNER OF FIRST MATCH IS {w1}")
time.sleep(3)



print(f"MATCH 1 : THE OG {player[2]} v/s THE GOAT {player[3]}")
time.sleep(1)
print("match in progresss..........")
time.sleep(5)

w2 = questionary.select(
    "who won?",
    choices=[
        player[2],
        player[3],
        "Draw",
    ]
).ask()

if w2 == "Draw":
    print(f"Time for rematch... {player[2]} v/s {player[3]}")
    w2 = questionary.select(
    "who won?",
    choices=[
        player[2],
        player[3],
    ]
).ask()
else:
    print(f"THE WINNER OF SECOND MATCH IS {w2}")
time.sleep(3)

print(f"NOW ITS TIME FOR THE UTIMATE FINAL BETWEEN {w1} V/S {w2}\nIt's time to check who is the real boss........")
time.sleep(2)
print(f"LET'S BEGAIN THE ULTIMATE BATTLE BETWEEN {w1} V/S {w2}")
time.sleep(2)
w = questionary.select(
    "who won the ultimate final?",
    choices=[
        w1,
        w2,
        "Draw",
    ]
).ask()


if w == "Draw":
    print(f"Time for rematch... {player[0]} v/s {player[1]}")
    w = questionary.select(
    "who won the ultimate rematch?",
    choices=[
        w1,
        w2,
    ]
).ask()
else:
    print(f"THE WINNER OF FINAL MATCH IS {w} ")

print(F"CONGRATULATIONS {w} ON WINNING THIS ULTIMATE TOURNAMENT!!")
time.sleep(2)
print(f"{player}, You all have played well.\nWe are proud of you all for playing fairly.")    
time.sleep(3)
print("THE END!")







