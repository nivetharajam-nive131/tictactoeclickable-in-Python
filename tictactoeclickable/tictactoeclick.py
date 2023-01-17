import pygame

# Initialize pygame and create a window
pygame.init()
size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")

# Load images
x_img = pygame.image.load("X.jpg")
o_img = pygame.image.load("O.jpg")

# Create a list to store the state of the squares
squares = [[0 for x in range(3)] for y in range(3)]

# Create a variable to store the current turn
turn = 0

# Function to draw the X or O on a square
def draw_x_o(pos):
    global turn
    if turn%2 == 0:
        screen.blit(x_img, (pos[0], pos[1]))
    else:
        screen.blit(o_img, (pos[0], pos[1]))
    turn += 1

# Function to handle mouse clicks
def on_mouse_click(pos):
    global squares
    # Convert the mouse position to grid coordinates
    column = pos[0] // 100
    row = pos[1] // 100
    # Check if the square is empty
    if squares[row][column] == 0:
        # Draw the X or O on the square
        draw_x_o((column * 100, row * 100))
        # Update the state of the square
        squares[row][column] = turn % 2+ 1
        # Check for a win or a draw
        check_win_or_draw()

# Function to check for a win or a draw
def check_win_or_draw():
    global squares
    # Check for a win
    for i in range(3):
        if squares[i][0] == squares[i][1] == squares[i][2] and squares[i][0] != 0:
            print("Player", squares[i][0], "wins!")
        if squares[0][i] == squares[1][i] == squares[2][i] and squares[0][i] != 0:
            print("Player", squares[0][i], "wins!")
    if squares[0][0] == squares[1][1] == squares[2][2] and squares[0][0] != 0:
        print("Player", squares[0][0], "wins!")
    if squares[0][2] == squares[1][1] == squares[2][0] and squares[0][2] != 0:
        print("Player", squares[0][2], "wins!")
    # Check for a draw
    if all(all(val != 0 for val in row) for row in squares):
        print("It's a draw!")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            on_mouse_click(event.pos)
    pygame.display.update()

# Clean up
pygame.quit()

