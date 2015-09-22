def dp(s, weight_target, memo):
    # the general idea is: for the left most slot, try to put a open bracket and close bracket, and for the recursive
    # call we should have a target (eg, starting with xxxx, we do dp('[xxx', -1) - target is -1 because that is
    # the balance we will need in the remaining string to be still balanced
    memo_key = (s, weight_target)

    if memo_key in memo:
        return memo[memo_key]

    # in this case, the rest of the string has negative weight. that is invalid.
    if weight_target > 0:
        result = 0
    else:
        # base cases
        if s == '':
            if weight_target == 0:
                result = 1
            else:
                result = 0
        else:
            if s[0] == 'x':
                count_open = dp(s[1:], weight_target-1, memo)  # add a [
                count_close = dp(s[1:], weight_target+1, memo)  # add a ]
            elif s[0] == '[':
                count_open = dp(s[1:], weight_target-1, memo)  # add a [
                count_close = 0
            else:  # must be s[0] == ']'
                count_open = 0
                count_close = dp(s[1:], weight_target+1, memo)  # add a ]

            result = count_open + count_close

    memo[memo_key] = result
    return result


def solve(n, ks):
    s = ['x']*(2*n) # x = free to use [ or ]
    for fixed_char in ks:
        s[fixed_char-1] = '['

    s = ''.join(s)

    return dp(s, 0, {})

# sample input
#print solve(1, [1]) == 1
#print solve(1, [2]) == 0
#print solve(3, [2]) == 3
#print solve(4, [5,7]) == 2

# large input

#print solve(19, [5])


number_of_cases = int(raw_input())
for case_number in xrange(number_of_cases):
    n, _ = map(int, raw_input().split())
    ks = map(int, raw_input().split())
    print solve(n, ks)

