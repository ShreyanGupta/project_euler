from collections import defaultdict
import time

if __name__ == "__main__":
    digit_map = defaultdict(set)
    for i in range(10**5):
        cube = i ** 3
        cube_digit = str(sorted(str(cube)))
        digit_map[cube_digit].add(i)
        if len(digit_map[cube_digit]) >= 4:
            print(cube_digit, len(digit_map[cube_digit]), digit_map[cube_digit])

    print("PRINTING ALL 5 CUBE SET")
    for digits, cube_set in digit_map.items():
        if len(cube_set) == 5:
            print(digits, cube_set)