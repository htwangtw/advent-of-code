from aoc.tools import read_input
import re

path = "2020/data/day14.txt"

data = read_input(path)

mask = 36 * "X"
mem = {}
for line in data:
    cmd, _, val = line.split()
    if cmd=='mask':
        mask = val
    else:
        val = "{:036b}".format(int(val))
        result = "".join(m if m in "01" else v for v, m in zip(val, mask))
        addr = re.search("^mem\[(\d+)\]", cmd).group(1)
        mem[int(addr)] = int(result, 2)

print(sum(mem.values()))

def find_floats(results):
    for addr in results:
        i = addr.find('X')
        if i == -1:
            return [addr]
        zero = find_floats([addr[:i] + str(0) + addr[i+1:]])
        one = find_floats([addr[:i] + str(1) + addr[i+1:]])
        return zero + one


mask = 36 * "X"
mem_loc = {}
for line in data:
    cmd, _, val = line.split()
    if cmd=='mask':
        mask = val
    else:
        addr = re.search("^mem\[(\d+)\]", cmd).group(1)
        addr = "{:036b}".format(int(addr))
        result = "".join(m if m in "X1" else v for v, m in zip(addr, mask))
        results =  find_floats([result])
        for addr in results:
            deci = int(addr, 2)
            mem_loc[deci] = int(val)

print(sum(mem_loc.values()))