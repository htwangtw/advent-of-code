with open("input", "r") as f:
    data = f.read().split("\n\n")

players = []
for player in data:
    player = list(map(int, player.splitlines()[1:]))
    players.append(player)

def game(p1, p2):
    if not all([p1, p2]):
        return p1, p2
    winner, loser = (p1, p2)[p2[0] > p1[0]], (p1, p2)[p2[0] < p1[0]]
    winner += [winner.pop(0), loser.pop(0)]
    return game(winner, loser)


def cal_result(player):
    return sum(p * i for p, i in zip(player, range(len(player), 0, -1)))

p1, p2 = players
p1, p2 = game(p1, p2)
print(max(cal_result(p1), cal_result(p2)))


def recursive_combat(p1, p2):
    decks_p1, decks_p2 = set(), set()
    while p1 and p2:
        cur_deck_1, cur_deck_2 = tuple(p1), tuple(p2)
        if cur_deck_1 in decks_p1 and cur_deck_2 in decks_p2:
            return [1], []
        decks_p1.add(cur_deck_1)
        decks_p2.add(cur_deck_2)

        check1 = p1.pop(0)
        check2 = p2.pop(0)

        if len(p1) >= check1 and len(p2) >= check2:
            # recursive game here
            sub_p1, sub_p2 = recursive_combat(p1[: check1], p2[:check2])
            if sub_p1:
                p1 += [check1, check2]
            else:
                p2 += [check2, check1]
        else: # the normal check
            if check1 > check2:
                p1 += [check1, check2]
            else:
                p2 += [check2, check1]
    return p1, p2

with open("input", "r") as f:
    data = f.read().split("\n\n")


test = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".split("\n\n")

players = []
for player in data:
    player = list(map(int, player.splitlines()[1:]))
    players.append(player)

p1, p2 = players
p1, p2 = recursive_combat(p1, p2)
print(max(cal_result(p1), cal_result(p2)))