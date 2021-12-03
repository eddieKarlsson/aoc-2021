def _most_common_bit(li, inverse=False):
    is_true_cnt = 0
    is_false_cnt = 0

    for i in li:
        if i:
            is_true_cnt += 1
        else:
            is_false_cnt += 1

    if not inverse:
        if is_true_cnt > is_false_cnt:
            return True
        else:
            return False
    if inverse:
        if is_true_cnt > is_false_cnt:
            return False
        else:
            return True


def _convert_bitlist_to_int(li):
    bin_rep = '0b'

    for bit in li:
        if bit:
            bin_rep = bin_rep + '1'
        else:
            bin_rep = bin_rep + '0'

    return int(bin_rep, 2)


def part1(input_file):
    list_of_lists = []
    list_is_created = False
    for line in open(input_file):
        line = line.strip()
        binary_length = len(line)
        for bit in range(binary_length):
            # Create the same number of list as the length as the binary string
            if not list_is_created:
                for i in range(binary_length):
                    list_of_lists.append([])
                list_is_created = True

            # Convert str to bit and append to list
            bit_state = True if line[bit] == '1' else False
            list_of_lists[bit].append(bit_state)

    # Get gamma rate bit sequence
    gamma_rate = []
    epsilon_rate = []
    for li in list_of_lists:
        gamma_rate.append(_most_common_bit(li))
        epsilon_rate.append(_most_common_bit(li, inverse=True))

    gamma_rate_dec = _convert_bitlist_to_int(gamma_rate)
    epsilon_rate_dec = _convert_bitlist_to_int(epsilon_rate)

    print(f'gamma_rate:{gamma_rate_dec}\tepsilon_rate:{epsilon_rate_dec}')
    return gamma_rate_dec * epsilon_rate_dec


if __name__ == '__main__':
    print(part1('input.txt'))
