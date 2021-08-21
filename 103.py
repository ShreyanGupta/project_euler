def check_n(seq, n):
    return True

def get_range(seq):
    max_limit = seq[0] + seq[1]
    curr_limit = max_limit
    i, j = 2, len(seq) - 1
    while i < j:
        curr_limit += seq[i]
        curr_limit -= seq[j]
        i += 1
        j -= 1
        max_limit = min(max_limit, curr_limit)
    return (max_limit, seq[-1] + 1)

def build_seq(seq):
    if len(seq) == 0:
        for i in range(1, 10):
            yield [i]

    elif len(seq) == 1:
        for i in range(seq[0] + 1, 10):
            seq.append(i)
            yield seq
            seq.pop

    else:
        max_n, min_n = get_range(seq)
        for n in range(min_n, max_n + 1):
            seq.append(n)
            if check_seq(seq):
                yield seq
            seq.pop()

if __name__ == "__main__":
    for s1 in build_seq([]):
        for s2 in build_seq(s1):
            for s3 in build_seq(s2):
                print(s3)