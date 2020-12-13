from aoc.tools import read_input

path = "2020/data/day13.txt"

def parse_rules(path):
    time, ids = read_input(path)
    return int(time), ids.split(",")

time = 939
instr = "7,13,x,x,59,x,31,19".split(",")

time, instr = parse_rules(path)

bus_no = []
time_to_next = []
for i in instr:
    if i != "x":
        time_since_last = time % int(i)
        wait_for_next = int(i) - time_since_last
        bus_no.append(int(i))
        time_to_next.append(wait_for_next)

next_bus = min(time_to_next)

for i, t in enumerate(time_to_next):
    if t == next_bus:
        print(bus_no[i] * t)

# part 2
# I swear this is what I learned in school
bus_id_mod = [(i, int(bus_id)) for i, bus_id in enumerate(instr, start=0) if bus_id != "x"]
start = time
M = 1
for mod, m in bus_id_mod:
    M *= m

# find a * b === 1 mode with pow
res = sum(-mod * pow((M // m), -1, m) * (M // m) for mod, m in bus_id_mod) % M
print(res)