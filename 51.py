import copy
import sympy

p_max = 156003000
# p_max = 1500
primes_list = sympy.primerange(1, p_max)
# primes_set = set(primes_list)

print("Start")

def get_template_list(n):
    str_num = str(n)
    template_list = []
    for digit in range(10):
        zero_pos = [i for i, c in enumerate(str_num) if c == str(digit)]
        if(len(zero_pos) < 3):
            continue
        for i in range(len(zero_pos)):
            for j in range(i+1, len(zero_pos)):
                for k in range(j+1, len(zero_pos)):
                    x, y, z = zero_pos[i], zero_pos[j], zero_pos[k]
                    template_list.append(str_num[0:x] + '*' + str_num[x+1:y] + '*' + str_num[y+1:z] + '*' + str_num[z+1:])
    return template_list


def get_num_list(template):
    for i in range(10):
        yield int(template.replace('*', str(i)))

# print(get_template_list(1000111))
# print(list(get_num_list("11**11")))

template_set = set()

for p in primes_list:
    for t in get_template_list(p):
        if t in template_set:
            continue
        template_set.add(t)
        count = 0
        for num in get_num_list(t):
            count += sympy.isprime(num)
        if count > 7:
            for num in get_num_list(t):
                print("!!", num, sympy.isprime(num))
                count += sympy.isprime(num)
            print(t, count)

# x = 0
# r = 156003
# for i in range(r):
#     x += sympy.isprime(i)

# print(x)