"""
Drone-Themed Python Warmup
Task: Write a Python script that simulates a drone moving in 3D space.
The script should keep track of the drone’s position (x, y, z),
accept a sequence of commands (e.g., ["forward 5", "left 3", "up 2", "backward 1", "stop"]),
update the position with basic math, and print the updated state after each command.
The drone should remain inside a cubic boundary (e.g., 10×10×10),
log its full trajectory, and detect collisions with a few fixed obstacles inside the box.
"""
import random

n = 10

matrix = [[["." for _ in range(n)] for _ in range(n)] for _ in range(n)]

num_obstacles = random.randint(1, n ** 3 // 4)

for _ in range(num_obstacles):
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    z = random.randint(0, n - 1)
    matrix[x][y][z] = "█"


while True:
    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)
    z = random.randint(0, n - 1)

    if matrix[x][y][z] == ".":
        matrix[x][y][z] = "D"
        drone_position = [x, y, z]
        break


def print_layer():
    drone_z = drone_position[2]

    for y in range(n):
        row = ""

        for x in range(n):
            row += f"{matrix[x][y][drone_z]}  "

        print(row)

    print()


while True:
    print_layer()

    print("Drone location:", tuple(drone_position))

    command = input("Enter command or 'stop': ").strip().lower()

    if command == "stop":
        break

    parts = command.split()

    if len(parts) != 2 or not parts[1].isdigit():
        print("Invalid. Example command: forward 3")
        continue

    direction = parts[0]
    steps = int(parts[1])

    for _ in range(steps):
        drone_x, drone_y, drone_z = drone_position
        x, y, z = drone_x, drone_y, drone_z

        if direction == "forward":
            y -= 1
        elif direction == "backward":
            y += 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1
        elif direction == "up":
            z += 1
        elif direction == "down":
            z -= 1
        else:
            print("Unknown direction!")
            break

        if 0 <= x < n and 0 <= y < n and 0 <= z < n and matrix[x][y][z] != "█":
            matrix[drone_x][drone_y][drone_z] = "."
            matrix[x][y][z] = "D"
            drone_position = [x, y, z]

        else:
            print("Trajectory is blocked! Make another command.")
            break
