import random
import json
import os

def input_int(text: str, min=1, max=3) -> int:
    while True:
        try:
            output = int(input(text))
            if output < min or output > max:
                print("Keine richtige eingabe!")
            else:
                return output
        except KeyboardInterrupt:
            return None
        except:
            print("Keine richtige eingabe!")

def count_sublist_occurrences(lst, sublst):
    count = 0
    sub_len = len(sublst)
    for i in range(len(lst) - sub_len + 1):
        if lst[i:i + sub_len] == sublst:
            count += 1
    return count

def find_sublist_positions(lst, sublst):
    positions = []
    sub_len = len(sublst)
    for i in range(len(lst) - sub_len + 1):
        if lst[i:i + sub_len] == sublst:
            positions.append(i)
    return positions

def find_petern(last_moves: list, lenge:int=5):
    patern = []
    if len(last_moves) >= lenge:
        for ofset in range(len(last_moves) - lenge):
            petern = []
            for index in range(lenge):
                petern.append(last_moves[index + ofset])
            progras = True
            for data in patern:
                if petern == data["petern"]:
                    progras = False
            if progras == True:
                count = count_sublist_occurrences(last_moves, petern)
                data = {
                    "petern": petern,
                    "count": count
                }
                patern.append(data)
    return patern

def find_best_move(paterns: list, last_moves: list, lenge:int=5):
    last_5_moves = last_moves[-lenge:]
    patern_think = 0
    for index in range(len(paterns)):
        #print(paterns[index])
        if paterns[index]["petern"] == last_5_moves:
            patern_think = index
    data = paterns[patern_think]
    #print(data["petern"])
    positions = find_sublist_positions(last_moves, data["petern"])
    if len(positions) >= 2:
        potential_move = []
        for position in positions:
            try:
                potential_move.append(last_moves[position + lenge])
            except Exception as e:
                #print(e)
                pass
        try:
            move = potential_move[random.randint(0, len(potential_move) - 1)]
            #print(move)
            return move
        except ValueError:
            return None

    else:
        return None

def find_move(paterns: list, last_moves: list, lenge:int=5):
    higest = 0
    higest_index = 0
    for index in range(len(paterns)):
        if paterns[index]["count"] > higest:
            higest = paterns[index]["count"]
            higest_index = index
    position = find_sublist_positions(last_moves, paterns[higest_index]["petern"])[-1]
    try:
        move = last_moves[position + lenge]
    except IndexError:
        try:
            move = last_moves[position + lenge]
        except IndexError:
            return None
    return move

def find_winning_move(move: int):
    SSP = [2, 3, 1]
    return SSP[move - 1]

def ai_move(last_moves: list) -> int:
    paterns = find_petern(last_moves)
    if paterns != []:
        move = find_best_move(paterns, last_moves)
        if move == None:
            move = find_move(paterns, last_moves)
            if move == None:
                move = random.randint(1, 3)
    else:
        move = random.randint(1, 3)

    return find_winning_move(move)

def find_win(ai_move: int, move: int):
    global points_you, points_ai, ties
    global language, lang
    ai_move -= 1
    move -= 1
    if ai_move == move:
        ties += 1
        return f"{language[lang][8][2]}!"
    else:
        if move == 0:
            if ai_move == 1:
                points_ai += 1
                return language[lang][11][0]
            elif ai_move == 2:
                points_you += 1
                return language[lang][11][1]
        if move == 1:
            if ai_move == 2:
                points_ai += 1
                return language[lang][11][0]
            elif ai_move == 0:
                points_you += 1
                return language[lang][11][1]
        if move == 2:
            if ai_move == 0:
                points_ai += 1
                return language[lang][11][0]
            elif ai_move == 1:
                points_you += 1
                return language[lang][11][1]

def S_S_P(last_moves: list = []) -> list:
    global points_you, points_ai, ties
    global lang, language
    SSP = language[lang][7]
    games = 0
    while True:
        games += 1
        move = ai_move(last_moves)
        number = input_int(f"1-{SSP[0]} 2-{SSP[1]} 3-{SSP[2]} ({language[lang][8][0]}: {points_ai}, {language[lang][8][1]}: {points_you}, {language[lang][8][2]}: {ties}, {language[lang][8][3]}: {games}): ", min=0)
        if number != None and number != 0:
            last_moves.append(number)
        if number == None or number == 0:
            return last_moves
        print()
        print(f"{language[lang][8][1]}:", SSP[number - 1])
        print(f"{language[lang][8][0]}:", SSP[move - 1])
        print()
        print(find_win(move, number))
        print("\n----------------------------\n")

points_you = 0
points_ai = 0
ties = 0
last_moves = []

lang = input_int("1-Deutsch, 2-English: ", max=2) - 1
print()

language = [
    [
        "Gib deinen Benutzernamen an: ",
        "Welchen Benutzer willst du löschen: ",
        "wird gelöscht.",
        "erfolgreich gelöscht.",
        "Der Benutzer exsistiert nicht!",
        "KI daten vorhanden.",
        "Kein KI daten vorhanden.",
        ["Schere", "Stein", "Papier"],
        [
            "KI",
            "Du",
            "Unentschieden",
            "Spiel"
        ],
        "Spiechere die KI daten auf den Profil.",
        "KI daten erfolgreich gespeichert.",
        [
            "Die KI hat gewonnen!",
            "Du hast gewonnen!"
        ],
        "löschen"
    ],
    [
        "Enter your username: ",
        "Which user do you want to delete: ",
        "is deleted.",
        "successfully deleted.",
        "The user does not exist!",
        "AI data available.",
        "No AI data available.",
        ["Scissors", "Stone", "Paper"],
        [
            "AI",
            "You",
            "draw",
            "game"
        ],
        "Save the AI ​​data to the profile.",
        "AI data saved successfully.",
        [
            "The AI ​​has won!",
            "You won!"
        ],
        "delet"
    ]
]

while True:
    profil = input(language[lang][0]).lower()
    if profil == language[lang][12]:
        profile = input(language[lang][1]).lower()
        if os.path.exists(f"ai\\{profile}.json"):
            print(f"{profile}.json", language[lang][2])
            os.remove(f"ai\\{profile}.json")
            print(f"{profile}.json", language[lang][3], "\n")
        else:
            print(language[lang][4])
    else:
        break

if os.path.exists(f"ai\\{profil}.json"):
    print(language[lang][5])
    with open(f"ai\\{profil}.json", "r", encoding="utf-8") as file:
        last_moves = json.load(file)
        print(last_moves)
else:
    print(language[lang][6])
print("\n----------------------------\n")

last_moves = S_S_P(last_moves)

print(language[lang][9])
with open(f"ai\\{profil}.json", "w", encoding="utf-8") as file:
    json.dump(last_moves, file, indent=4)
print(language[lang][10],"\n")
