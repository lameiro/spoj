# def generate_table(base):
# l = []
#     exponent = 0
#     while True:
#         result = (base ** exponent) % 10
#
#         if result in l:
#             offset = l.index(result)
#             break
#
#         l.append(result)
#         exponent += 1
#
#     return l[offset:], offset
#
# print '{'
# for i in xrange(10):
#     print '    %d: %s' % (i, generate_table(i))
# print '}'



# # tests
# from input
# print solve(3, 10) == 9
# print solve(6, 2) == 6
#

# my own
# print solve(0, 0) == (0 ** 0) % 10
# print solve(0, 1) == (0 ** 1) % 10
# print solve(1, 1) == (1 ** 1) % 10
# print solve(0, 9) == (0 ** 9) % 10
# print solve(11, 18) == (11 ** 18) % 10
# print solve(22, 27) == (22 ** 27) % 10
# print solve(43, 46) == (43 ** 46) % 10
# print solve(54, 15) == (54 ** 15) % 10
# print solve(55, 4) == (55 ** 4) % 10
# print solve(96, 93) == (96 ** 93) % 10
# print solve(107, 22) == (107 ** 22) % 10
# print solve(1008, 21) == (1008 ** 21) % 10
# print solve(49, 1000) == (49 ** 1000) % 10