import copy
import time
tps=time.time()


map_input_raw = open("data.txt", "r").readlines()
aled=0

map_input = [list(i[:-1]) for i in map_input_raw]

def test_case(map_input2):
    global aled
    compteur=0
    guard_pos=[]
    for i, line in enumerate(map_input2):
        if "^" in line:
            guard_pos = [i, line.index("^")]


    def str_map():
        oui = "".join(["".join(i) + "\n" for i in map_input2])
        print(oui)


    directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    exit_maze = False
    act_direction = "up"
    while not exit_maze:
        if compteur==10000:
            aled+=1
            break
        next_guard_pos = [
            guard_pos[0] + directions[act_direction][0],
            guard_pos[1] + directions[act_direction][1],
        ]
        if 0 <= next_guard_pos[0] < len(map_input2) and 0 <= next_guard_pos[1] < len(
            map_input2[0]
        ):
            if map_input2[next_guard_pos[0]][next_guard_pos[1]] != "#":
                map_input2[guard_pos[0]][guard_pos[1]] = "X"
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
            map_input2[guard_pos[0]][guard_pos[1]] = "X"
            exit_maze = True
        compteur+=1

cp_map_input=copy.deepcopy(map_input)
oui=copy.deepcopy(map_input)
for a,data in enumerate(map_input):
    for y in range(len(data)):
        cp_map_input[a][y]="#" if cp_map_input[a][y]=="." else cp_map_input[a][y]
        test_case(cp_map_input)
        cp_map_input=copy.deepcopy(map_input)
    
        
print(aled)

print(time.time()-tps)

