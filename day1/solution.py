with open('input.txt') as f:
    input_list = [line.rstrip() for line in f]


def larger_than_previous_measurement(input_file):
    count = 0
    previous = None
    for line in open(input_file):
        line = line.strip()
        current = int(line)
        if previous and current > previous:
            count += 1
        previous = current
    return count


if __name__ == '__main__':
    print(larger_than_previous_measurement('input.txt'))
