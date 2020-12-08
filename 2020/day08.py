from aoc.tools import read_input
import re

path = "2020/data/day08.txt"

def parse_input(path):
    data = read_input(path)
    boot_code = []
    for line in data:
        instruction, move = line.split()
        boot_code.append((instruction, int(move)))
    return boot_code

boot_code = parse_input(path)

# Immediately before any instruction is executed a second time,
# what value is in the accumulator?

def operate(op_rule, start, acc):
    if op_rule[0] == "acc":
        start += 1
        acc += op_rule[1]
    elif op_rule[0] == "jmp":
        start += op_rule[1]
    else:
        start += 1
    return start, acc

op_path = []
start = 0
acc = 0
while start not in op_path:
    op_path.append(start)
    start, acc = operate(boot_code[start], start, acc)
print(acc)

# jmp <-> nop that will end the operation
# acc number

for i , (instruction, move) in enumerate(boot_code):
    if instruction != "acc":
        new_op = boot_code.copy()
        if instruction == "nop":
            new_op[i] = ("jmp", move)
        elif instruction == "jmp":
            new_op[i] = ("nop", move)

        op_path = []
        start = 0
        acc = 0
        while start not in op_path:
            op_path.append(start)
            start, acc = operate(new_op[start], start, acc)
            if start == len(new_op):
                print(acc)
                break
