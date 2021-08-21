
def rev_add(n):
    return n + int(str(n)[::-1])

def is_palindrome(n):
    str_n = str(n)
    return str_n == str_n[::-1]

non_lychrel = 0
total = 0
limit = 10000
for n in range(1, limit):
    x = n
    total += 1
    for i in range(51):
        print(x, end=" -> ")
        x = rev_add(x)
        if is_palindrome(x):
            non_lychrel += 1
            print(x, "======", n)
            break

print("Total: ", total - non_lychrel)