def solve(men, women):
    return sum(m * w for m, w in zip(sorted(men), sorted(women)))


#print solve([1,4,2], [3,1,2]) == 4*3 + 2*2 + 1*1

nr_of_cases = int(raw_input())

for i in xrange(nr_of_cases):
    _ = int(raw_input()) # nr of people, not used
    men = map(int, raw_input().split())
    women = map(int, raw_input().split())

    print solve(men, women)
