from collections import defaultdict

# mapping from sum last2, last digit => num numbers

def gen_first_map():
    mapping = defaultdict(int)
    for i in range(1, 10):
        for j in range(10):
            if i + j > 9:
                continue
            mapping[(i+j, j)] += 1
    return mapping

def gen_next_map(old_mapping):
    new_mapping = defaultdict(int)
    for k,v in old_mapping.items():
        num = str(k[0] - k[1]) + str(k[1])
        x, y = k
        for z in range(10 - x):
            ext_num = num + str(z)
            print((y+z, z), ext_num)
            new_mapping[(y+z, z)] += v
    return new_mapping

if __name__ == "__main__":
    curr_map = gen_first_map()

    for i in range(2, 20):
        print(i)
        curr_map = gen_next_map(curr_map)

    s = 0
    for v in curr_map.values():
        s += v
    print(s)
