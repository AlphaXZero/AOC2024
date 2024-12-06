import time

map_input_raw = open("data.txt", "r").readlines()

map_input = [list(i[:-1]) for i in map_input_raw]
guard_pos=[]
for i, line in enumerate(map_input):
    if "^" in line:
        guard_pos = [i, line.index("^")]


def str_map():
    oui = "".join(["".join(i) + "\n" for i in map_input])
    print(oui)


directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
exit_maze = False
act_direction = "up"
while not exit_maze:
    next_guard_pos = [
        guard_pos[0] + directions[act_direction][0],
        guard_pos[1] + directions[act_direction][1],
    ]
    if 0 <= next_guard_pos[0] < len(map_input) and 0 <= next_guard_pos[1] < len(
        map_input[0]
    ):
        if map_input[next_guard_pos[0]][next_guard_pos[1]] != "#":
            map_input[guard_pos[0]][guard_pos[1]] = "X"
            guard_pos = next_guard_pos
        else:
            match act_direction:
                case "up":
                    act_direction = "right"
                case "down":
                    act_direction = "left"
                case "left":
                    act_direction = "up"
                case "right":
                    act_direction = "down"
    else:
        map_input[guard_pos[0]][guard_pos[1]] = "X"
        str_map()
        exit_maze = True

tot_x = 0
tot_x = sum([i.count("X") for i in map_input])

print(tot_x)
