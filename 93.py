import itertools

def bin_num(a, b):
    x = set({a+b, a-b, a*b})
    if b != 0:
        x.add(a/b)
    return x

def bin_set(set_a, set_b):
    all_num_set = set()
    for x in set_a:
        for y in set_b:
            all_num_set |= bin_num(x, y)
    return all_num_set


def expression(*num_set_list):
    if len(num_set_list) == 1:
        return num_set_list[0]

    all_num_set = set()
    for i in range(1, len(num_set_list)):
        left_set = expression(*num_set_list[:i])
        right_set = expression(*num_set_list[i:])
        all_num_set |= bin_set(left_set, right_set)
    return all_num_set


def all_combinations(*num_list):
    all_num_set = set()
    for perm in itertools.permutations(num_list):
        num_set_list = [{x} for x in perm]
        all_num_set |= expression(*num_set_list)
    return all_num_set


def filter_set(*num_list):
    all_num_set = all_combinations(*num_list)
    # all_num_set = sorted(list(filter(lambda x: x > 0, all_num_set)))
    reduced_list = []
    for n in all_num_set:
        if int(n) == n and n > 0:
            reduced_list.append(int(n))
    reduced_list.sort()
    i = 0
    while i+1 == reduced_list[i]:
        i += 1
    # print(num_list, reduced_list)
    return i


if __name__ == "__main__":
    # print(from2(4,5))
    # print(bin_set(set({2}), set({5})))
    # print(filter_set(1, 2, 3, 4))
    i_max = 0
    for combi in itertools.combinations([1,2,3,4,5,6,7,8,9], 4):
        i = filter_set(*combi)
        if i >= i_max:
            i_max = i
            print("FOUND NEW MAX", i, combi)