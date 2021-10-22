import random

print("****Welcome to Minesweeper****")

#def game_size()


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



#def game_loop():
 #   recursive...
#while True
 #   print


#command = flag or clear
#phase de jeu()


#### -1 = game over
#### flag replaces cover

### uncover 0 uncovers adjacent 0


#####---------------------------------------------

## create empty gameboard
grid = []
for i in range(height):
    grid.append([0] * width)

## distribute mines
for i in range(mines):
    random_height = random.randrange(0, height)
    random_width = random.randrange(0, width)
    grid[random_height][random_width] = -1

print(*grid, sep='\n')
# populate squares
for x in range (len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == -1:
            if y < len(grid[x]):
                grid[x][y+1] += 1
            if y < len(grid[x]):

           # if x < len(x):
              #  pass
                #x+1[y] +=1
   # i += 1
print("-------------")
print(*grid, sep='\n')

# draw hidden grid
j = 0
for i in range(width):
    print(i+1, end=" ")
for x in grid:
    if j == 0:
        print("", sep="\n")
    else:
        print(j, sep="\n")
    j += 1
    for y in x:
        print("█", end=" ")
print(j)



# move prompt
chosen_line = 0
chosen_column = 0

while True:
    chosen_line = int(input("Pick your square. Enter line number: "))
    if 0 <= chosen_line > height+1:
        print("Invalid line")
    else:
        break

while True:
    print("You've chosen line ", chosen_line, ".", sep="", end=" ")
    chosen_column = int(input("Enter column number: "))
    if 0 <= chosen_column > width+1:
        print("Invalid column")
    else:
        break

# action prompt
while True:
    print("You've chosen square ", chosen_line, " x ", chosen_column, ".", sep="", end=" ")
    command = input("\nPress C to clear\nPress F to flag/unflag")
    #if command == F or command == f:
   #     pass
    #if command == C or command == c:
     #   pass
    #else:
     #   (print("Please enter a valid command"))



#print("█", end=" ")
#print(j)


