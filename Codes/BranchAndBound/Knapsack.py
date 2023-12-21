from queue import Queue

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

def compare(a):
    return a.value / a.weight

def bound(u, n, W, arr):
    if u.weight >= W:
        return 0

    profitBound = u.profit
    j = u.level + 1
    totWeight = u.weight

    while j < n and totWeight + arr[j].weight <= W:
        totWeight += arr[j].weight
        profitBound += arr[j].value
        j += 1

    if j < n:
        profitBound += (W - totWeight) * arr[j].value / arr[j].weight

    return profitBound

def knapsack_solution(W, arr, n):
    arr.sort(key=compare, reverse=True)
    q = Queue()
    u = Node(-1, 0, 0, 0)
    q.put(u)

    maxProfit = 0
    pruning_count = 0

    while not q.empty():
        u = q.get()

        if u.level == -1:
            v = Node(0, 0, 0, 0)
        elif u.level == n - 1:
            continue

        v = Node(u.level + 1, u.profit + arr[u.level + 1].value, 0, u.weight + arr[u.level + 1].weight)

        if v.weight <= W:
            if v.profit > maxProfit:
                maxProfit = v.profit
            v.bound = bound(v, n, W, arr)
            if v.bound > maxProfit:
                q.put(v)
            else:
                pruning_count += 1
                print(f"Pruned at node {v.level} with items considered: {v.level + 1}, Bound: {v.bound}, MaxProfit: {maxProfit}")

        v = Node(u.level + 1, u.profit, 0, u.weight)
        v.bound = bound(v, n, W, arr)

        if v.bound > maxProfit:
            q.put(v)
        else:
            pruning_count += 1
            print(f"Pruned at node {v.level} without including item {v.level + 1}, Bound: {v.bound}, MaxProfit: {maxProfit}")

    print(f"Total prunings: {pruning_count}")
    return maxProfit

W = 10
arr = [Item(2, 40), Item(3.14, 50), Item(1.98, 100), Item(5, 95), Item(3, 30)]
n = len(arr)

print('Maximum possible profit =', knapsack_solution(W, arr, n))
