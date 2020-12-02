def read_passcode(path):
    with open(path, "r") as f:
        passcode_book = []
        for l in f.readlines():
            l = l.split()
            ub, lb = map(int, l[0].split("-"))
            entry = {"rule": (ub, lb),
                     "word": l[1].split(":")[0],
                     "password": l[2]}
            passcode_book.append(entry)

    return passcode_book

passcode_book = read_passcode("2020/data/day02.txt")

# part 1
count = 0
for entry in passcode_book:
    word_occurence = entry["password"].count(entry["word"])

    if (word_occurence >= entry["rule"][0]) and (word_occurence <= entry["rule"][1]):
        count += 1

print(count)

# prart 2
count = 0
for entry in passcode_book:
    p1, p2 = entry["rule"]
    if len(entry["password"]) < p1:
        first_word, second_word = None
    elif len(entry["password"]) < p2:
        first_word = entry["password"][p1 - 1]
        second_word = None
    else:
        first_word = entry["password"][p1 - 1]
        second_word = entry["password"][p2 - 1]

    if (first_word, second_word).count(entry["word"]) == 1:
        count += 1

print(count)