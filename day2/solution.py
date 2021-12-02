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

    print(f'Part1:\nHorizontal={horizontal_pos}\tDepth={depth_pos}')

    return horizontal_pos * depth_pos


def part2(input_file):
    horizontal_pos = 0
    depth_pos = 0
    aim_pos = 0
    for line in open(input_file):
        cmd_list = line.split()
        cmd = cmd_list[0]
        n_moves = int(cmd_list[1])

        if cmd == 'forward':
            horizontal_pos += n_moves
            depth_pos += n_moves * aim_pos
        elif cmd == 'down':
            aim_pos += n_moves
        elif cmd == 'up':
            aim_pos -= n_moves

    print(f'Part2:\nHorizontal={horizontal_pos}\tDepth={depth_pos}')

    return horizontal_pos * depth_pos


if __name__ == '__main__':
    #  print(part1('input.txt'))
    print(part2('input.txt'))
