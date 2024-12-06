oui = open("data.txt", "r").readlines()


rules = {}

for i, line in enumerate(oui[: oui.index("\n")]):
    if line[: line.index("|")] not in rules:
        rules[line[: line.index("|")]] = [line[line.index("|") + 1 : -1]]
    else:
        rules[line[: line.index("|")]] += [line[line.index("|") + 1 : -1]]

text_input = [i[:-1].split(",") for i in oui[oui.index("\n") + 1 :]]

good_lines = []

for i, line in enumerate(text_input):
    passe = set()
    is_ok = True
    for j, num in enumerate(line):
        passe.add(num)
        for x in passe:
            if num in rules and x in rules[num]:
                is_ok = False
                break
    if is_ok:
        good_lines.append(line)

result = [int(i[len(i) // 2]) for i in good_lines]

print(sum(result))
