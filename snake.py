WIDTH = 20
HEIGHT = 10

def draw(snake, food):
    # Clear the screen so each frame replaces the last
    print("\033[H\033[J", end="")

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if col == 0 or col == WIDTH - 1:
                print("#", end="")        # side walls
            elif row == 0 or row == HEIGHT - 1:
                print("#", end="")        # top/bottom walls
            elif (col, row) == food:
                print("*", end="")        # food
            elif (col, row) == snake[0]:
                print("O", end="")        # snake head
            elif (col, row) in snake[1:]:
                print("o", end="")        # snake body
            else:
                print(" ", end="")        # empty space
        print()                           # newline at end of each row


if __name__ == "__main__":
    snake = [(5, 5), (4, 5), (3, 5)]     # head first, then body
    food = (10, 5)
    draw(snake, food)
