def fact(index):
    prod = 1
    for i in range(2, index + 1):
        prod *= i
    return prod

def price(index, blue):
    if index == blue:
        print(index, blue, 1)
        return 1
    if blue == 0:
        print(index, blue, fact(index + 1))
        return fact(index + 1)
    x = price(index - 1, blue - 1)
    y = index * price(index - 1, blue)
    print(index, blue, x + y)
    return x + y

if __name__ == "__main__":
    r = price(15, 8)
    print(r, fact(16) / r)