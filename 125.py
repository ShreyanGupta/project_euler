from collections import defaultdict

f_map = dict()

def f(x):
    global f_map
    if x not in f_map:
        f_map[x] = x * (x + 1) * (2*x + 1) // 6
    return f_map[x]

def is_palindrome(x):
    x = str(x)
    return x == x[::-1]

if __name__ == "__main__":
    nums = defaultdict(int)
    for i in range(1, 10**4):
        for j in range(i - 1):
            x = f(i) - f(j)
            if x < 10**8 and is_palindrome(x):
                print(x, i, j)
                nums[x] += 1
    s = 0
    for k,v in nums.items():
        s += k
        if v > 1:
            print("!!!", k, v)
    print("AND THE SUM ISSSSSS", s)