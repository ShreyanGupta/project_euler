from collections import defaultdict

def get_partition(end):
    if end == 0:
        return [set()]
    elif end == 1 or end == -1:
        return []

    p1 = get_partition(end - 2)
    p2 = get_partition(end - 3)

    for p in p1:
        p.add(end - 2)
    for p in p2:
        p.add(end - 3)

    return p1 + p2

def build_compatibility_set(partitions, partition_index):
    compatibility_set = defaultdict(set)
    for p1 in partitions:
        for p2 in partitions:
            if len(p1 & p2) == 0:
                x = partition_index[p1]
                y = partition_index[p2]
                compatibility_set[x].add(y)
    return compatibility_set


dp = dict()

def get_count(p, index, compatibility_set):
    if (p, index) in dp:
        if index > 7:
            print("used", index, p)
        return dp[(p, index)]
    if index == 0:
        return 1
    s = 0
    for q in compatibility_set[p]:
        s += get_count(q, index - 1, compatibility_set)
    dp[(p, index)] = s
    return s


if __name__ == "__main__":
    partitions = get_partition(32)

    print("building partitions")
    partition_index = dict()
    for i in range(len(partitions)):
        partitions[i].remove(0)
        partitions[i] = frozenset(partitions[i])
        partition_index[partitions[i]] = i + 1
        # print(partitions[i])
    print(len(partitions))

    print("building compatitibility set")
    compatibility_set = build_compatibility_set(partitions, partition_index)
    compatibility_set[0] = set(range(1, len(partitions) + 1))
    # for k,v in compatibility_set.items():
        # print(k, v)

    print("getting count")
    x = get_count(0, 10, compatibility_set)
    print(x)