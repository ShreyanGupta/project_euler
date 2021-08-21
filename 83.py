import numpy as np
import heapq


matrix = [[]]
cost = [[]]
x = 0
y = 0
heap = []


def read_matrix(file_name):
    global cost
    global matrix
    global x
    global y
    with open(file_name, "r") as f:
        matrix = f.read()
    matrix = list(map(lambda x: list(map(int, x.strip().split(","))), matrix.strip().split("\n")))
    x, y = len(matrix), len(matrix[0])
    cost = np.full((x, y), 10**9, dtype=int)

def read_matrix2():
    global cost
    global matrix
    global x
    global y
    matrix = [
        [131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331]
    ]
    x, y = len(matrix), len(matrix[0])
    cost = np.full((x, y), 10**9, dtype=int)


def update(i, j, side_value):
    if i == -1 or j == -1 or i == x or j == y:
        return
    new_cost = side_value + matrix[i][j]
    if new_cost < cost[i][j]:
        cost[i][j] = new_cost
        heapq.heappush(heap, (new_cost, i, j))


def process():
    curr_cost, i, j = heapq.heappop(heap)
    if cost[i][j] < curr_cost:
        return
    print(i, j, curr_cost)
    update(i + 1, j, curr_cost)
    update(i - 1, j, curr_cost)
    update(i, j + 1, curr_cost)
    update(i, j - 1, curr_cost)


if __name__ == "__main__":
    read_matrix("p083_matrix.txt")
    # read_matrix2()
    cost[0][0] = matrix[0][0]
    print(cost)
    print(matrix)

    heapq.heappush(heap, (matrix[0][0], 0, 0))
    while heap:
        process()

    print(cost)
