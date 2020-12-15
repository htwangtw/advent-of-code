starting_num = [20, 9, 11, 0, 1, 2]

def memory_game(spoken_num, target):
    starting_num = spoken_num.copy()

    if len(starting_num) == target:
        return starting_num[-1]
    idx = len(starting_num)
    curr_num = starting_num[-1]
    find = [i for i, t in enumerate(starting_num) if t == curr_num]
    curr_num = 0 if len(find) == 1 else idx - find[-2] - 1
    starting_num.append(curr_num)
    return memory_game(starting_num, target)
print(memory_game(starting_num, 2020))

starting_num = [20, 9, 11, 0, 1, 2]
# part 2 - cannot use recursion
def memo_game(spoken_num, turns):
    starting_num = spoken_num.copy()
    history = {value: i + 1 for i, value in enumerate(starting_num)}
    previous = list(history)[-1]
    for turn in range(len(history), turns):
        history[previous], previous = turn, turn - history.get(previous, turn)
    return previous

print(memo_game(starting_num, 2020))
print(memo_game(starting_num, 30_000_000))