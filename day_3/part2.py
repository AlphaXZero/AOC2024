import re

inp = open("data.txt", "r").read()
while "don't()" in inp:
    dont_ind = inp.find("don't()")
    do_ind = inp.find("do()", dont_ind)
    inp = inp[:dont_ind] + inp[do_ind + 4 :] if do_ind != -1 else inp[:dont_ind]
lis = re.findall(r"mul\((\d+),(\d+)\)", inp)
lis = map(lambda x: int(x[0]) * int(x[1]), lis)
print(sum(lis))
