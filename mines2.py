import random
print("****Welcome to Minesweeper****")

height = 0
while height <= 2:
    height = int(input("Enter game board height: "))
    if height <= 2:
        print("That's too easy! Please enter a higher number.")

width = 0
while width <= 2:
    width = int(input("Enter game board width: "))
    if width <= 2:
        print("That's too easy! Please enter a higher number.")

mines = 0
while True:
    mines = int(input("Enter number of mines: "))
    if mines <= 1:
        print("That's too easy! Please enter a higher number.")
        continue
    if mines >= height*width-1:
        print("Too many mines! Please enter a lower number.")
        continue
    break

# intialisation des tableaux en fonction des inputs height et width
base_table = [width * [0]]
game_board = [width * ["█"]]

for i in range(height - 1):
    base_table.append(width * [0])
    game_board.append(width * ["█"])


# fonctions d'affichage des deux tableaux
def base_table_display():
    for i in range(height):
        print(base_table[i])


def game_board_display():
    j = 1
    for i in range(width):
        print(i+1, end=" ")
    print("")
    for i in range(width):
        print("—", end=" ")
    print("")
    for i in range(height):

        print(*game_board[i], "|",j, sep=" ", end="\n")
        j += 1






# placement aléatoire des mines
# il faut gérer le cas ou la génération aléatoire des coordonnés pointe deux fois de suite sur la même case
for i in range(mines):
    x = random.randint(0, height - 1)
    y = random.randint(0, width - 1)
    if base_table[x][y] != "m":
        base_table[x][y] = "m"
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i >= 0 and i < height and j >= 0 and j < width and base_table[i][j] != "m":
                    base_table[i][j] += 1

# visualisation des états initiaux de game_board et base_table
base_table_display()
game_board_display()


# fonction récursive gérant la découverte automatique des 0 adjacent à un autre et s'arrétant au premier chiffre
def show(H, W):
    if base_table[H][W] != 0:
        game_board[H][W] = base_table[H][W]
    else:
        game_board[H][W] = " "

        for i in range(H - 1, H + 2):
            for j in range(W - 1, W + 2):
                print(j)
                if i >= 0 and i < height and j >= 0 and j < width:
                    if game_board[i][j] == "█":
                        show(i, j)


continue_game = True
while continue_game == True:
    input_H = 0
    input_W = 0
    input_type = ""
    input_result = base_table[input_H][input_W]
    while True:
        input_H = int(input("Pick your square. Enter line number: ")) - 1
        if 0 <= input_H > height:
            print("Invalid line")
        else:
            break

    while True:
        print("You've chosen line ", input_H + 1, ".", sep="", end=" ")
        input_W = int(input("Enter column number: ")) - 1
        if 0 <= input_W > width:
            print("Invalid column")
        else:
            break

    while True:
        print("You've chosen square ", input_H + 1, " x ", input_W + 1, ".", sep="", end=" ")
        input_type = input("\nPress C to clear\nPress F to flag\nPress U to unflag ---> ")

        if input_type != "F" and input_type != "f" and input_type != "C" and input_type != "c":
            (print("Please enter a valid command"))
        else:
            break

    input_result = base_table[input_H][input_W]

    # Cas ou on uncover une case sans mines adjacentes
    if input_result == 0 and input_type == "C":
        show(input_H, input_W)
    elif (input_result == "m" or input_result == "mflag") and input_type == "C":
        game_board[input_H][input_W] = "BOOM"
    elif input_result == "Flaged" and input_type == "C":
        game_board[input_H][input_W] = input_result
    elif input_type == "F":
        game_board[input_H][input_W] = "F"
        if base_table[input_H][input_W] == "m":
            base_table[input_H][input_W] = "mflag"
    elif input_type == "U":
        game_board[input_H][input_W] = "█"
        if input_result == "mflag":
            base_table[input_H][input_W] = "m"
        elif game_board[input_H][input_W] != "F":
            print("la case n'est pas flagué")
    else:
        game_board[input_H][input_W] = input_result
    base_table_display()
    game_board_display()
    # conditions de fin du jeu
    if mines == sum([i.count("mflag") for i in base_table]) and mines == sum([i.count("F") for i in game_board]) or any(
            "BOOM" in sublist for sublist in game_board):
        continue_game = False

if any("BOOM" in sublist for sublist in game_board):
    print("****** YOU LOOSE ******")
else:
    print("***** YOU WIN ******")

# il manque la possibilité de rejouer une partie
