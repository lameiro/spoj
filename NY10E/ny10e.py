# Nice and readable recursion, but quite slow. Memoizing helps, but the iterative still wins
# def dp(starting_with, num_digits):
#     if num_digits == 1:
#         return 1
#     else:
#         the_sum = 0
#         for suffix in xrange(starting_with, 10):
#             the_sum += dp(suffix, num_digits-1)
#
#         return the_sum
#
# def dp_non_recursive(num_digits):
#     return dp(0, num_digits+1)

def dp_iterative(num_digits):
    previous_level = next_level = [1]*10
    for i in xrange(1, num_digits+1):
        next_level = [sum(previous_level[i:]) for i in xrange(10)]
        previous_level = next_level

    return next_level[0]

number_of_cases = int(raw_input())

for i in xrange(number_of_cases):
    case_number, number_of_digits = map(int, raw_input().split())
    print case_number, dp_iterative(number_of_digits)