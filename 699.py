def get_pow3():
    pow3 = []
    for i in range(1, 100):
        x = 3 ** i - 1
        if x > 10**14:
            return pow3
        pow3.append(x)

def get_alpha(pow3_array):
    alpha_array = []
    for x in pow3_array:
        alpha = -1
        while x % 2 == 0:
            alpha += 1
            x /= 2
        alpha_array.append(alpha)
    return alpha_array

if __name__ == "__main__":
    pow3_array = get_pow3()
    print(pow3_array)
    alpha_array = get_alpha(pow3_array)
    print(alpha_array)