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


def sum3_larger_than_previous_measurement(input_file):
    with open(input_file) as f:
        input_list = [int(line.rstrip()) for line in f]

    for i, item in enumerate(input_list):
        # Create list of three summed values
        print(type(i), i)
        print(type(item))
        print(type(input_list))

        if i < len(input_list) - 1:
            print(input_list[i + 1])
        #  sum = i + input_list[i + 1] + input_list[i + 2]


if __name__ == '__main__':
    #  print(larger_than_previous_measurement('input.txt'))
    print(sum3_larger_than_previous_measurement('input_test.txt'))
