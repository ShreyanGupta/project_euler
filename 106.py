def fact(x):
    prod = 1
    for i in range(2, x+1):
        prod *= i
    return prod

def combi(n, c):
    return fact(n) // fact(c) // fact(n-c)

def total(n):
    return (3 ** n - 2 * (2 ** n) + 1) //2

def non_test(n):
    s1 = 0
    s2 = 0
    for i in range(2, n+1, 2):
        s1 += combi(n, i)
        s2 += combi(n, i//2) * combi(n-i//2, i//2) // 2
        print("?",i, s1, s2)
    return s1, s2

if __name__ == "__main__":
    print(non_test(4))