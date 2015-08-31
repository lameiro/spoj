def solve(seq1, seq2):
    # add sentinel to avoid having to special case the end of loop below
    sentinel = 10001
    seq1.append(sentinel)
    seq2.append(sentinel)

    seq1_dict = {v: i for i, v in enumerate(seq1)}  # for fast lookup. maybe a binary search would be better...
    seq2_dict = {v: i for i, v in enumerate(seq2)}

    linked_numbers = sorted(set(seq1).intersection(seq2))

    the_sum = 0
    prev_seq1_index = 0
    prev_seq2_index = 0

    for linked_number in linked_numbers:
        next_seq1_index = seq1_dict[linked_number]
        next_seq2_index = seq2_dict[linked_number]

        sum_seq1 = sum(seq1[prev_seq1_index:next_seq1_index+1])
        sum_seq2 = sum(seq2[prev_seq2_index:next_seq2_index+1])

        if sum_seq1 > sum_seq2:
            the_sum += sum_seq1
        else:
            the_sum += sum_seq2

        prev_seq1_index = next_seq1_index + 1 # skip for the next iteration of the loop
        prev_seq2_index = next_seq2_index + 1

    return the_sum - sentinel


# Example inputs
# c1_1 = map(int, '3 5 7 9 20 25 30 40 55 56 57 60 62'.split())
# c1_2 = map(int, '1 4 7 11 14 25 44 47 55 57 100'.split())
#
# c2_1 = map(int, '-5 100 1000 1005'.split())
# c2_2 = map(int, '-12 1000 1001'.split())
#
# print solve(c1_1, c1_2)
# print solve(c2_1, c2_2)

while True:
    sequence1 = map(int, raw_input().split())[1:]  # strip the count
    if sequence1 == []:
        break
    sequence2 = map(int, raw_input().split())[1:]
    print solve(sequence1, sequence2)