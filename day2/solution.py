def part1(input_file):
    horizontal_pos = 0
    depth_pos = 0
    for line in open(input_file):
        cmd_list = line.split()
        cmd = cmd_list[0]
        n_moves = int(cmd_list[1])

        if cmd == 'forward':
            horizontal_pos += n_moves
        elif cmd == 'down':
            depth_pos += n_moves
        elif cmd == 'up':
            depth_pos -= n_moves

    print(f'Horizontal={horizontal_pos}\tDepth={depth_pos}')

    return horizontal_pos * depth_pos


def part2(input_file):
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
    print(part1('input_test.txt'))
    #  print(part2('input.txt'))
