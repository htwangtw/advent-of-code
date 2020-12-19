from aoc.tools import read_input

data = read_input("2020/data/day19.txt")

test = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb

""".splitlines()

def parse_info(data):
    rules = {}
    messages = []
    for l in data:
        if ":" in l:
            key, instr = l.split(": ")
            key = int(key)
            if instr[0] == '"':
                rules[key] = instr[1]
            else:
                content = [tuple(map(int, seq.split(' ')))
                           for seq in instr.split(' | ')]
                rules[key] = content
        elif len(l) > 0:
            messages.append(l)
    return rules, messages

def check(rules, key, message, pos):
    rule = rules[key]
    if type(rule) is str:
        if pos < len(message) and rule == message[pos]:
            return {pos + 1}
        else:
            return set()
    else:
        endings = set()
        for subrule in rule:
            buffer = {pos}
            for item in subrule:
                tmp = set()
                for loc in buffer:
                    tmp = tmp | check(rules, item, message, loc)
                buffer = tmp
            endings = endings | buffer
        return endings

rules, messages = parse_info(data)
results = [len(m) in check(rules, 0, m, 0) for m in messages]
print(results.count(True))

rules[8] = [([42]), (42, 8)]
rules[11] = [(42, 31), (42, 11, 31)]
results = [len(m) in check(rules, 0, m, 0) for m in messages]
print(results.count(True))