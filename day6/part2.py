data = {}
with open('input.txt') as f:
    li = [int(x) for x in f.readline().split(',')]
    for value in range(max(9, max(li))):
        data[value] = 0  # set all keys increment
    for i in li:
        data[i] += 1

for days in range(256):
    zeroes = data[0]
    data[0] = 0
    for index in range(1, len(data)):
        data[index-1] += data[index]
        data[index] = 0
    data[6] += zeroes
    data[8] += zeroes

val = data.values()
ans = sum(val)
print(f'Part2: Answer: {ans}')
