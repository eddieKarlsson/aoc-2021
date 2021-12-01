p1 = 0
p2 = None
prev = None

idx = 0
for line in open('input.txt'):
    line = line.strip()
    x = int(line)
    if prev and x > prev:
        p1 += 1
    prev = x

print(p1)
