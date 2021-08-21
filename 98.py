from collections import defaultdict
import math
import itertools

def read_text(filename):
    with open(filename) as f:
        content = f.read()
    word_array = content.replace("\"", "").split(",")
    word_array.sort(key=len, reverse=True)
    return word_array


def sort_word_array(word_array):
    word_dict = defaultdict(set)
    for word in word_array:
        word_dict[len(word)].add(word)
    return word_dict


def get_sq(limit):
    sq_set = set()
    limit = int(math.sqrt(limit))
    print(limit, limit ** 2)
    for i in range(limit + 1):
        sq_set.add(str(i ** 2))
    return sq_set


def is_anagram(w1, w2):
    if w1 == w2 or len(w1) != len(w2):
        return False
    x = defaultdict(int)
    for l in w1:
        x[l] += 1
    for l in w2:
        x[l] -=1
        if x[l] == -1:
            return False
    return True


def add_to_trie(trie, word):
    if len(word) == 0:
        trie[True] = True
    else:
        if word[0] not in trie:
            trie[word[0]] = dict()
        add_to_trie(trie[word[0]], word[1:])


def make_trie(trie, word_set):
    for word in word_set:
        add_to_trie(trie, word)


def is_in_trie(trie, word):
    if len(word) == 0:
        return 0 in trie
    if word[0] not in trie:
        return False
    return is_in_trie(trie[word[0]], word[1:])


def get_sub_trie(trie, partial_word):
    if len(partial_word) == 0:
        return trie
    if partial_word[0] not in trie:
        return dict()
    return get_sub_trie(trie[partial_word[0]], partial_word[1:])



def check_sq2(assignment, w1, w1_trie, w2, w2_trie):
    if len(w1) == 0:
        # Termination case
        # print("TERMINATION CASE")
        return True in w1_trie and True in w2_trie

    l = w1[0]
    # print(assignment, w1, l, w2)
    if l in assignment:
        if assignment[l] in w1_trie:
            return check_sq2(assignment, w2, w2_trie, w1[1:], w1_trie[assignment[l]])
        else:
            return False
    else:
        for i in {'0','1','2','3','4','5','6','7','8','9'}:
            if i not in w1_trie:
                continue
            if i in assignment.values():
                continue
            assignment[l] = i
            if check_sq2(assignment, w2, w2_trie, w1[1:], w1_trie[i]):
                return True
            del assignment[l]
    return False


def check_base(word1, word2, trie):
    # print("Checking for", word1, word2)
    partial_assignment = dict()
    possible = check_sq2(partial_assignment, word1, trie, word2, trie)
    num1, num2 = -1, -1
    if possible:
        num1 = ''.join([partial_assignment[l] for l in word1])
        num2 = ''.join([partial_assignment[l] for l in word2])
    print(possible, num1, num2, word1, word2, partial_assignment)


# def check_sq(partial_assignment, rem_set, w1, w1_trie, w2, w2_trie):
#     if len(w1) == 0:
#         # Termination case
#         print("TERMINATION CASE")
#         return True in w1 and True in w2

#     l1, l2 = w1[0], w2[0]
#     n1, n2 = partial_assignment.get(l1, -1), partial_assignment.get(l2, -1)
#     print(partial_assignment, w1, w2, l1, l2, n1, n2)

#     rem_set_elt = list(rem_set)


#     # Both letters are assigned
#     if n1 != 1 and n2 != -1:
#         if n1 not in w1_trie or n2 not in w2_trie:
#             return False
#         else:
#             return check_sq(partial_assignment, rem_set, w1[1:], w1_trie[n1], w2[1:], w2_trie[n2])
#     # n1 is assigned
#     elif n1 != -1:
#         for n2 in rem_set_elt:
#             rem_set.remove(n2)
#             partial_assignment[l2] = n2
#             if check_sq(partial_assignment, rem_set, w1[1:], w1_trie[n1], w2[1:], w2_trie[n2]):
#                 return True
#             del partial_assignment[l2]
#             rem_set.add(n2)
#     # n2 is assigned
#     elif n2 != -1:
#         for n1 in rem_set_elt:
#             rem_set.remove(n1)
#             partial_assignment[l1] = n1
#             if check_sq(partial_assignment, rem_set, w1[1:], w1_trie[n1], w2[1:], w2_trie[n2]):
#                 return True
#             del partial_assignment[l1]
#             rem_set.add(n1)
#     # both are unassigned but l1 = l2
#     elif l1 == l2:
#         for n in rem_set_elt:
#             rem_set.remove(n)
#             partial_assignment[l1] = n
#             if check_sq(partial_assignment, rem_set, w1[1:], w1_trie[n], w2[1:], w2_trie[n]):
#                 return True
#             del partial_assignment[l1]
#             rem_set.add(n1)
#     # both are unassigned and distinct
#     else:
#         for n1 in rem_set_elt:
#             rem_set.remove(n1)
#             partial_assignment[l1] = n1
#             for n2 in rem_set_elt:
#                 if n1 == n2:
#                     continue
#                 rem_set.remove(n2)
#                 partial_assignment[l2] = n2
#                 if check_sq(partial_assignment, rem_set, w1[1:], w1_trie[n1], w2[1:], w2_trie[n2]):
#                     return True
#                 del partial_assignment[l2]
#                 rem_set.add(n2)
#             del partial_assignment[l1]
#             rem_set.add(n1)
#     return False



if __name__ == "__main__":
    word_array = read_text("p098_words.txt")
    word_dict = sort_word_array(word_array)
    print(word_dict.keys())

    sq_set = get_sq(10**10)
    trie = dict()
    make_trie(trie, sq_set)

    for k, words in word_dict.items():
        print("LENGTH: ", k)
        for w1 in words:
            for w2 in words:
                if is_anagram(w1, w2):
                    letter_set = set([l for l in w1])
                    # print(len(letter_set), w1, w2, letter_set)
                    check_base(w1, w2, trie)



    # partial_assignment = dict()
    # check_sq2(partial_assignment, "CARE", trie, "RACE", trie)
    # print(partial_assignment)