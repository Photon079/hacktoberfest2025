import curses
import random

# Initialize the screen
screen = curses.initscr()
curses.curs_set(0)  # hide cursor
height, width = 20, 60
win = curses.newwin(height, width, 0, 0)  # create a window
win.keypad(1)
win.timeout(150)  # refresh time in ms

# Snake and food initial position
snake_x = width // 4
snake_y = height // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [height // 2, width // 2]
win.addch(food[0], food[1], curses.ACS_PI)  # ACS_PI = food symbol

key = curses.KEY_RIGHT  # initial direction

score = 0

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # Calculate new head
    head = snake[0][:]
    if key == curses.KEY_DOWN:
        head[0] += 1
    elif key == curses.KEY_UP:
        head[0] -= 1
    elif key == curses.KEY_LEFT:
        head[1] -= 1
    elif key == curses.KEY_RIGHT:
        head[1] += 1

    # Game over conditions
    if head in snake or head[0] in [0, height] or head[1] in [0, width]:
        curses.endwin()
        print(f"Game Over! Score: {score}")
        break

    snake.insert(0, head)

    # Eating food
    if head == food:
        score += 1
        food = None
        while food is None:
            nf = [random.randint(1, height - 2), random.randint(1, width - 2)]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Move snake: remove tail
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)  # draw head
