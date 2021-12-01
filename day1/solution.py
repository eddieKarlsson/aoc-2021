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

    # Create list of three summed values
    sum3_list = []
    for i, item in enumerate(input_list):
        sum = item
        if i < len(input_list) - 1:
            sum += input_list[i + 1]
        if i < len(input_list) - 2:
            sum += input_list[i + 2]
        sum3_list.append(sum)
        # print(sum)

    #  Count if the current summed value is greater than last
    count = 0
    previous = None
    for current in sum3_list:
        if previous and current > previous:
            count += 1
        previous = current

    return count


if __name__ == '__main__':
    print(larger_than_previous_measurement('input.txt'))
    print(sum3_larger_than_previous_measurement('input.txt'))
