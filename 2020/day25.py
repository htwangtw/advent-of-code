input = """17115212
3667832
"""

data = tuple(map(int, input.splitlines()))

subject = 7
loop = 0
divisor = 20201227
start = 1

while start != data[0]:
    start = (start * subject) % divisor
    loop = loop + 1

print(pow(data[1], loop, divisor))