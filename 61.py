from itertools import permutations

set_list = [set()] * 9

for i in range(500):
    s3 = i * (i+1) // 2
    s4 = i * i
    s5 = i * (3*i-1) // 2
    s6 = i * (2*i-1)
    s7 = i * (5*i-3) // 2
    s8 = i * (3*i-2)
    if s3 > 999 and s3 < 10000: set_list[3].add(s3)
    if s4 > 999 and s4 < 10000: set_list[4].add(s4)
    if s5 > 999 and s5 < 10000: set_list[5].add(s5)
    if s6 > 999 and s6 < 10000: set_list[6].add(s6)
    if s7 > 999 and s7 < 10000: set_list[7].add(s7)
    if s8 > 999 and s8 < 10000: set_list[8].add(s8)


l_set = [dict()] * 9
# r_set = [dict()] * 9

for i in range(3,9):
    for elt in set_list[i]:
        l_set[i][elt // 100] = elt % 100
        # r_set[i][elt % 100] = elt

print(l_set[3])

for perm in permutations(range(3,6)):
    print(perm)
    perm = list(perm) + [perm[0]]
    open_set = l_set[perm[0]].keys()
    for i, index in enumerate(perm):
        print(i, index, open_set)
        open_set = set([l_set[index][k] for k in open_set])
        open_set &= l_set[perm[i+1]].keys()