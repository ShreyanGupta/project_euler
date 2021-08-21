import sympy
import copy
import time

def is_remarkable(p1, pset):
    for p2 in pset:
        concat1 = int(str(p1) + str(p2))
        concat2 = int(str(p2) + str(p1))
        if not sympy.isprime(concat1) or not sympy.isprime(concat2):
            return False
    return True


# (sum, count) -> set(set(prime))
remarkable_prime_dict = dict()

def get_remarkable_prime(prime_sum, num_prime):
    # for given prime_sum, return list(list_prime)
    if (prime_sum, num_prime) in remarkable_prime_dict:
        return remarkable_prime_dict[(prime_sum, num_prime)]

    if num_prime == 1:
        if sympy.isprime(prime_sum):
            remarkable_prime_dict[(prime_sum, num_prime)] = frozenset({frozenset({prime_sum})})
        else:
            remarkable_prime_dict[(prime_sum, num_prime)] = frozenset({})
        return remarkable_prime_dict[(prime_sum, num_prime)]

    rpset = set()
    for p in sympy.sieve.primerange(0, prime_sum):
        # print(p, prime_sum, get_remarkable_prime(prime_sum - p, num_prime - 1))
        for pset in get_remarkable_prime(prime_sum - p, num_prime - 1):
            if is_remarkable(p, pset):
                new_set = set(pset)
                new_set.add(p)
                rpset.add(frozenset(new_set))
    remarkable_prime_dict[(prime_sum, num_prime)] = frozenset(rpset)
    return remarkable_prime_dict[(prime_sum, num_prime)]


# sum_max = 10000
# for psum in range(1, sum_max):
#     plist = get_remarkable_prime(psum, 4)
#     # print(psum, plist)
#     if plist:
#         print(psum, plist)


# print(remarkable_prime_dict)

    # for p1 in sympy.sieve.primerange(0, sum_max):
    #     for p2 in sympy.sieve.primerange(0, sum_max):
    #         for p3 in sympy.sieve.primerange(0, sum_max):


# sum_max = 100000
# depth = 4
# dp = []

# for num_prime in range(depth):
#     dp.append([None] * sum_max)

# for psum in range(sum_max):
#     dp[0][psum] = [[psum]] if sympy.isprime(psum) else []
#     for num_prime in range(1, depth):
#         dp[num_prime][psum] = []
#         for p in sympy.sieve.primerange(0, psum):
#             # print(p, num_prime, psum - p, dp[num_prime - 1][psum - p], num_prime - 1, psum - p)
#             for plist in dp[num_prime - 1][psum - p]:
#                 if p >= max(plist) and is_remarkable(p, plist):
#                     dp[num_prime][psum].append(plist + [p])
#         if num_prime >= 3 and dp[num_prime][psum]: print("dp", num_prime + 1, psum, dp[num_prime][psum])


def insert_trie(trie, word, prime_set):
    if word in prime_set:
        if "prime" not in trie:
            trie["prime"] = set()
        trie["prime"].add(word)

    if len(word) == 0:
        trie[True] = True
    else:
        if word[0] not in trie:
            trie[word[0]] = dict()
        insert_trie(trie[word[0]], word[1:], prime_set)


def get_trie(trie, word):
    if len(word) == 0:
        if True not in trie:
            return None
        else:
            return trie
    else:
        if word[0] not in trie:
            return None
        else:
            return get_trie(trie[word[0]], word[1:])


def get_remarkable_set(trie, prime):
    sub_trie = get_trie(trie, prime)
    if not sub_trie or "prime" not in sub_trie:
        return set()
    else:
        return sub_trie["prime"]

def get_remarkable_set_map(remarkable_set_map, trie):
    for prime in trie["prime"]:
        remarkable_set = get_remarkable_set(trie, prime)
        if len(remarkable_set) != 0:
            remarkable_set_map[prime] = remarkable_set
            # print(prime, remarkable_set)


def prune_remarkable_set_map(remarkable_set_map):
    keys = list(remarkable_set_map.keys())
    for p1 in keys:
        prime_set = remarkable_set_map[p1]
        reduced_set = set()
        while prime_set:
            p2 = prime_set.pop()
            if p2 in remarkable_set_map and p1 in remarkable_set_map[p2]:
                reduced_set.add(p2)
        if len(reduced_set) != 0:
            remarkable_set_map[p1] = reduced_set
            # print(p1, remarkable_set_map[p1])
        else:
            del remarkable_set_map[p1]


def advance_tier(x, remarkable_set_map):
    next_tier = set()
    for prime_set in x:
        p_set_list = []
        for p in prime_set:
            p_set = remarkable_set_map[p]
            p_set_list.append(p_set)
            # if not intersection_set:
            #     intersection_set = p_set
            # else:
            #     intersection_set &= p_set
        intersection_set = set.intersection(*p_set_list)
        # print("Int", prime_set, intersection_set)
        for p in intersection_set:
            prime_set_copy = set(prime_set)
            prime_set_copy.add(p)
            next_tier.add(frozenset(prime_set_copy))
    return next_tier


def make_base_tier(remarkable_set_map):
    base_tier = set()
    for p in remarkable_set_map.keys():
        base_tier.add(frozenset({p}))
    return base_tier


if __name__ == "__main__":
    prime_set = set()
    trie = dict()

    start_time = time.time()
    for p in sympy.sieve.primerange(0, 10**8):
        p = str(p)
        prime_set.add(p)
    end_time = time.time()
    print("Generated prime: time", end_time - start_time)

    start_time = time.time()
    for p in prime_set:
        insert_trie(trie, p, prime_set)
    end_time = time.time()
    print("Done generating trie: time", end_time - start_time)

    start_time = time.time()
    remarkable_set_map = dict()
    get_remarkable_set_map(remarkable_set_map, trie)
    prune_remarkable_set_map(remarkable_set_map)
    end_time = time.time()
    print("Done generating remarkable_set_map: time", end_time - start_time)

    start_time = time.time()
    base_tier = make_base_tier(remarkable_set_map)
    tier2 = advance_tier(base_tier, remarkable_set_map)
    # print(tier5)
    tier3 = advance_tier(tier2, remarkable_set_map)
    # print("tier3", tier3)
    tier4 = advance_tier(tier3, remarkable_set_map)
    # print("tier4", tier4)
    tier5 = advance_tier(tier4, remarkable_set_map)
    # print("tier5", tier5)
    end_time = time.time()
    print("Generated tier5", end_time - start_time)

    min_sum = 10**10
    min_set = None
    print("PRINTING ALL TIER 5")
    for p_set in tier5:
        s = 0
        for p in p_set:
            s += int(p)
        print(s, p_set)
        if s < min_sum:
            min_sum = s
            min_set = p_set

    print("MIN ONE", min_sum, min_set)