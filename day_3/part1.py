import re

inp = open("data.txt", "r").read()
lis = re.findall(r"mul\((\d+),(\d+)\)", inp)
lis = map(lambda x: int(x[0]) * int(x[1]), lis)
print(sum(lis))
