tab = open("data.txt", "r").read()
lines = tab.split("\n")
list_lines = [[int(i) for i in line.split()] for line in lines]
safe_count = 0
for line in list_lines:
    is_safe = True
    direction = 0
    for j in range(1,len(line)):
        actu_direction = -1 if line[j] - line[j - 1] > 0 else 1
        if  direction == 0:
            direction = actu_direction
        if (line[j-1] == line[j]
            or abs(line[j-1] - line[j]) > 3
            or direction != actu_direction
        ):
            is_safe = False
            break
    if is_safe:
        safe_count += 1
print(safe_count)
