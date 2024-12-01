f = open("input.txt", "r")
inp = f.read().split("\n")
dist = []
left = sorted([int(i[0 : i.index(" ")]) for i in inp])
right = sorted([int(i[i.index(" ") :]) for i in inp])
for i, leftdata in enumerate(left):
    dist += [leftdata - right[i]] if leftdata > right[i] else [right[i] - leftdata]
print(sum(dist))
