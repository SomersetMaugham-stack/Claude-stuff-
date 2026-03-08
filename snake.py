import time

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


def move(snake, direction):
    head_x, head_y = snake[0]           # unpack the head position

    if direction == "RIGHT":
        new_head = (head_x + 1, head_y)
    elif direction == "LEFT":
        new_head = (head_x - 1, head_y)
    elif direction == "UP":
        new_head = (head_x, head_y - 1)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 1)

    return [new_head] + snake[:-1]      # new head + old body, minus the tail


if __name__ == "__main__":
    snake = [(5, 5), (4, 5), (3, 5)]
    food = (10, 5)
    direction = "RIGHT"

    for _ in range(10):                 # run 10 frames then stop
        draw(snake, food)
        snake = move(snake, direction)
        time.sleep(0.2)                 # pause between frames so you can see it
