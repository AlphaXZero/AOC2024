f = open("input.txt", "r")
inp = f.read().split("\n")
dist = []
left = sorted([int(i[0 : i.index(" ")]) for i in inp])
right = sorted([int(i[i.index(" ") :]) for i in inp])
for i, leftdata in enumerate(left):
    dist += [abs(leftdata - right[i])]
print(sum(dist))
