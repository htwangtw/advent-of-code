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

def operate(instr, state):
    loc, acc = state
    if instr[0] == "acc":
        loc += 1
        acc += instr[1]
    elif instr[0] == "jmp":
        loc += instr[1]
    else:
        loc += 1
    return (loc, acc)

op_path = []
state = (0, 0)
while state[0] not in op_path:
    op_path.append(state[0])
    state = operate(boot_code[state[0]], state)
print(state[1])

# jmp <-> nop that will end the operation
# acc number

swap = {"jmp": "nop", "nop": "jmp"}
for i , (instruction, move) in enumerate(boot_code):
    if instruction != "acc":
        new_bc = boot_code.copy()
        new_bc[i] = (swap[instruction], move)

        op_path = []
        state = (0, 0)
        while state[0] not in op_path:
            op_path.append(state[0])
            state = operate(new_bc[state[0]], state)
            if state[0] == len(new_bc):
                print(state[1])
                break
