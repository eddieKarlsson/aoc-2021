list_of_lists = []
list_is_created = False
for line in open("input_test.txt"):
    line = line.strip()
    binary_length = len(line)
    for bit in range(binary_length):
        # Create the same number of list as the length as the binary string
        if not list_is_created:
            for i in range(binary_length):
                list_of_lists.append([])
            list_is_created = True

        list_of_lists[bit].append(line[bit])


#  def _find_most_common_bit(li):
