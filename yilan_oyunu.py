import random
import os
import sys
import time

# Oyun alanı boyutları
width = 20
height = 10

# Yılanın başlangıç konumu ve yönü
snake = [(5, 5), (5, 4), (5, 3)]
direction = 'RIGHT'
food = (random.randint(0, height - 1), random.randint(0, width - 1))
lives = 3  # Can hakkı

def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Can: {lives}")
    for y in range(height):
        for x in range(width):
            if (y, x) in snake:
                print('🐍', end='')
            elif (y, x) == food:
                print('🍎', end='')
            else:
                print(' ', end='')
        print()

def change_direction(new_direction):
    global direction
    if (direction == 'UP' and new_direction != 'DOWN') or \
       (direction == 'DOWN' and new_direction != 'UP') or \
       (direction == 'LEFT' and new_direction != 'RIGHT') or \
       (direction == 'RIGHT' and new_direction != 'LEFT'):
        direction = new_direction

def move_snake():
    global lives
    head_x, head_y = snake[0]
    if direction == 'UP':
        new_head = (head_x - 1, head_y)
    elif direction == 'DOWN':
        new_head = (head_x + 1, head_y)
    elif direction == 'LEFT':
        new_head = (head_x, head_y - 1)
    else:  # RIGHT
        new_head = (head_x, head_y + 1)

    # Çarpma kontrolü
    if new_head in snake or new_head[0] < 0 or new_head[0] >= height or new_head[1] < 0 or new_head[1] >= width:
        lives -= 1
        if lives == 0:
            print("Oyun Bitti! Kaybettiniz.")
            sys.exit()
        else:
            print("Çarpışma! Can kaybedildi. Yeniden başlatılıyor...")
            time.sleep(1)
            snake.clear()
            snake.extend([(5, 5), (5, 4), (5, 3)])
            place_food()
            return

    if new_head == food:
        snake.insert(0, new_head)
        place_food()
    else:
        snake.insert(0, new_head)
        snake.pop()

def place_food():
    global food
    while True:
        food = (random.randint(0, height - 1), random.randint(0, width - 1))
        if food not in snake:
            break

def main():
    global direction
    while True:
        print_board()
        new_direction = input("Yön (W/A/S/D): ").upper()
        if new_direction == 'W':
            change_direction('UP')
        elif new_direction == 'S':
            change_direction('DOWN')
        elif new_direction == 'A':
            change_direction('LEFT')
        elif new_direction == 'D':
            change_direction('RIGHT')
        move_snake()
        time.sleep(0.2)

if __name__ == "__main__":
    main()
