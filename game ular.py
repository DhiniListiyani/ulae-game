import curses
import random

# Inisialisasi layar menggunakan curses
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  # Membuat window dengan ukuran tertentu
win.keypad(1)  # Memungkinkan input keyboard
curses.noecho()  # Mencegah input muncul di layar
curses.curs_set(0)  # Menyembunyikan kursor
win.border(0)  # Membuat border di sekitar layar
win.timeout(100)  # Mengatur kecepatan permainan

# Posisi awal ular dan makanan
snake_x = 15
snake_y = 10
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]
food = [random.randint(1, 18), random.randint(1, 58)]
win.addch(food[0], food[1], '*')

# Awal gerakan ke kanan
key = curses.KEY_RIGHT
score = 0

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # Menghitung koordinat kepala ular
    if key == curses.KEY_DOWN:
        snake_y += 1
    elif key == curses.KEY_UP:
        snake_y -= 1
    elif key == curses.KEY_LEFT:
        snake_x -= 1
    elif key == curses.KEY_RIGHT:
        snake_x += 1

    # Memeriksa apakah ular menabrak border atau dirinya sendiri
    if (
        snake_y == 0 or snake_y == 19 or
        snake_x == 0 or snake_x == 59 or
        [snake_y, snake_x] in snake
    ):
        curses.endwin()
        print(f"Game Over! Skor Anda: {score}")
        break

    # Tambahkan posisi baru untuk kepala ular
    snake.insert(0, [snake_y, snake_x])

    # Cek apakah ular memakan makanan
    if snake_y == food[0] and snake_x == food[1]:
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, 18),
                random.randint(1, 58)
            ]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], '*')
    else:
        # Menghapus ekor ular
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    # Menggambar kepala ular
    win.addch(snake[0][0], snake[0][1], '#')

curses.endwin()