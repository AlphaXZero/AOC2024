f = open("input.txt", "r")
inp = f.read().split("\n")
left = [int(i[0 : i.index(" ")]) for i in inp]
right = sorted([int(i[i.index(" ") :]) for i in inp])
result = 0
for i in left:
    result += right.count(i) * i

print(result)
