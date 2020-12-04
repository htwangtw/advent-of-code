from aoc.tools import read_input


expense_report = read_input("2020/data/day01.txt")

# part 1
def find_sum(numbers, target_sum=2020):
    for i, n in enumerate(numbers):
        for m in numbers[i:]:
            if int(m) + int(n) == target_sum:
                return int(m) * int(n)

print(find_sum(expense_report))

# part 2
while expense_report:
    n = expense_report.pop()
    remainder = 2020 - int(n)
    try:
        answer = find_sum(expense_report, remainder) * int(n)
    except TypeError:
        continue
print(answer)
