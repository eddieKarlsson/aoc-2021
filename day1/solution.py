with open('input.txt') as f:
    input_list = [line.rstrip() for line in f]


def larger_than_previous_measurement(input_list):
    count = 0
    idx = 0
    for previous, current in zip(input_list, input_list[1:]):
        idx += 1
        will_count = False
        if current > previous:
            count += 1
            will_count = True
        print("current:", current, "previous:", previous, "\tindex:", idx, "increased?:", will_count, count)
    return count


if __name__ == '__main__':
    print(larger_than_previous_measurement(input_list))
