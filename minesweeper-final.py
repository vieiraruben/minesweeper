import random

print("**** WELCOME TO MINESWEEPER ****")


def game_size():
    # asks for board size and number of mines

    global height
    height = int(input("Enter game board height (minimum 3): "))
    while height <= 2:
        height = int(input("That's too easy! Please enter a higher number: "))

    global width
    width = int(input("Enter game board width (minimum 3): "))

    while width <= 2:
        width = int(input("That's too easy! Please enter a higher number: "))

    global mines
    mines = int(input("Enter number of mines (minimum 4): "))
    while not 3 < mines < height*width-1:
        if mines <= 3:
            mines = int(
                input("Not enough mines! Please enter a higher number: "))
        if mines >= height*width-1:
            mines = int(input("Too many mines! Please enter a lower number: "))


def create_board():
    # creates hidden game board
    global grid
    grid = []
    for i in range(height):
        grid.append([0] * width)

# distributes mines
    for i in range(mines):
        random_height = random.randrange(0, height)
        random_width = random.randrange(0, width)
        grid[random_height][random_width] = -1

# reveals hidden board:
# print(*grid, sep='\n')


def adjacent_cells():
    # populates cells
    global grid
    for i, line in enumerate(grid):
        for j, cell in enumerate(grid[i]):
            for k in range(-1, 2):
                if 0 <= j + k < width and 0 <= i - 1 < height and cell == -1 and grid[i-1][j + k] != -1:
                    grid[i-1][j + k] += 1
                if 0 <= j + k < width and 0 <= i < height and cell == -1 and grid[i][j + k] != -1:
                    grid[i][j + k] += 1
                if 0 <= j + k < width and 0 <= i + 1 < height and cell == -1 and grid[i+1][j + k] != -1:
                    grid[i+1][j + k] += 1


def create_game_board():
    # draws first game board
    global display_grid
    display_grid = []
    for i in range(height):
        display_grid.append(["█"] * width)


def draw_game_board():
    # draws game board

    j = 0
    for i in range(width):
        print(i+1, end=" ")
    for x in display_grid:
        if j == 0:
            print("", sep="\n")
        else:
            print(j, sep="\n")
        j += 1
        for y in x:
            if y == 0:
                print("█", end=" ")
            else:
                print(y, end=" ")
    print(j)


def move_prompt():
    # asks for cell choice

    global chosen_line
    global chosen_column

    chosen_line = int(input("Pick your cell. Please enter line number: "))
    while 0 <= chosen_line > height+1:
        chosen_line = int(input("Invalid line. Please enter line number: "))

    print("You've chosen line ", chosen_line, ".", sep="", end=" ")
    chosen_column = int(input("Enter column number: "))

    while 0 <= chosen_column > height+1:
        chosen_column = int(input("Invalid column. Enter column number: "))


def action_prompt():
    # asks for game move

    global chosen_line
    global chosen_column
    global move

    while True:
        print("You've chosen square ", chosen_line,
              " x ", chosen_column, ".", sep="", end=" ")
        move = input("\nPress C to clear\nPress F to flag/unflag\n--> ")
        if move != "F" and move != "f" and move != "C" and move != "c":
            (print("Please enter a valid command"))
        else:
            break

    chosen_line = chosen_line - 1
    chosen_column = chosen_column - 1


def adjacent_zeros(line, column):
    # reveals clear cells and adjacent numbers
    global display_grid

    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= column + i < width and 0 <= line + j < height and display_grid[line + j][column + i] != " ":
                if grid[line + j][column + i] == 0:
                    display_grid[line + j][column + i] = " "
                    adjacent_zeros(line + j, column + i)
                if grid[line + j][column + i] > 0:
                    display_grid[line + j][column +
                                           i] = grid[line + j][column + i]


def game_over():
    # reveals board if user hits mine
    global display_grid

    for x in range(height):
        for y in range(width):
            if grid[x][y] == -1:
                display_grid[x][y] = "M"
            else:
                display_grid[x][y] = " "


def clear(line, column):
    # clears cell
    global loss

    if grid[line][column] == -1:
        game_over()
        draw_game_board()
        loss = True

    if grid[line][column] > 0:
        display_grid[line][column] = grid[line][column]
        draw_game_board()

    if grid[line][column] == 0:
        adjacent_zeros(line, column)
        draw_game_board()


def flag(line, column):
    # flags/unflags cell
    if display_grid[line][column] == "F":
        display_grid[line][column] = "█"
    else:
        display_grid[line][column] = "F"


def win_check():
    # checks if user has won
    i = 0
    for x in range(height):
        for y in range(width):
            if display_grid[x][y] == "█" or (display_grid[x][y] == "F" and grid[x][y] == -1):
                i += 1

    return i != mines


def game_loop():
    # game sequence
    global loss
    loss = False

    game_size()
    create_board()
    adjacent_cells()
    create_game_board()
    draw_game_board()
    while win_check():
        move_prompt()
        action_prompt()
        if move == "C" or move == "":
            clear(chosen_line, chosen_column)
        if move == "F" or move == "f":
            flag(chosen_line, chosen_column)
            draw_game_board()
        if loss:
            print("Bomm, you've hit a mine!\n****** GAME OVER ******")
            break
    else:
        print("\n****************************\n********* YOU WIN **********\n****************************\n")


command = "Y"
while command == "Y":
    game_loop()
    command = input("Play again? Y/N ")
