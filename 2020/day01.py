def read_report(path):
    with open(path, "r") as f:
        expense_report = [int(l) for l in f.read().splitlines()]
    return expense_report

expense_report = read_report("data/day_01.txt")

# part 1
def find_sum(numbers, target_sum=2020):
    for i, n in enumerate(numbers):
        for m in numbers[i:]:
            if m + n == target_sum:
                return m * n

print(find_sum(expense_report))

# part 2
while expense_report:
    n = expense_report.pop()
    remainder = 2020 - n
    try:
        answer = find_sum(expense_report[i:], remainder) * n
    except TypeError:
        continue
print(answer)
