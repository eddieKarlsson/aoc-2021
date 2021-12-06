with open('input.txt') as f:
    initial_state = [int(x) for x in f.readline().strip('\n').split(',')]


def lanternfish(fish_index, population_li, new_day=True):
    if new_day:
        population_li[fish_index] -= 1
    if new_day and population_li[fish_index] <= -1:
        population_li[fish_index] = 6
        population_li.append(8)


fish_li = list(initial_state)
print(f'Initial state: {fish_li}')
days = 80
for day in range(1, days+1):
    for i in range(len(fish_li)):
        lanternfish(i, fish_li)
    print(f'After: {day} days: {fish_li}')

print(f'Part1: Answer: {len(fish_li)}')
