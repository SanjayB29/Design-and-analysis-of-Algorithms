from queue import Queue

# Define an Item class to represent each item in the knapsack
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

# Define a Node class to represent each node in the branch and bound tree
class Node:
    def __init__(self, level, profit, bound, weight):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.weight = weight

# Define a compare function to sort items by their value-to-weight ratio in descending order
def compare(a):
    return a.value / a.weight

# Define a function to calculate the maximum possible profit for a given node
def bound(u, n, W, arr):
    if u.weight >= W:
        return 0

    profitBound = u.profit
    j = u.level + 1
    totWeight = int(u.weight)

    while j < n and totWeight + int(arr[j].weight) <= W:
        totWeight += int(arr[j].weight)
        profitBound += arr[j].value
        j += 1

    if j < n:
        profitBound += int((W - totWeight) * arr[j].value / arr[j].weight)

    return profitBound

# Define the knapsack_solution function that uses the Branch and Bound algorithm
# to solve the 0-1 Knapsack problem
def knapsack_solution(W, arr, n):
    arr.sort(key=compare, reverse=True)
    q = Queue()
    u = Node(-1, 0, 0, 0)
    q.put(u)

    maxProfit = 0

    while not q.empty():
        u = q.get()

        if u.level == -1:
            v = Node(0, 0, 0, 0)

        if u.level == n - 1:
            continue

        v = Node(u.level + 1, u.profit + arr[u.level + 1].value, 0, u.weight + arr[u.level + 1].weight)

        if v.weight <= W and v.profit > maxProfit:
            maxProfit = v.profit

        v.bound = bound(v, n, W, arr)

        if v.bound > maxProfit:
            q.put(v)

        v = Node(u.level + 1, u.profit, 0, u.weight)

        v.bound = bound(v, n, W, arr)

        if v.bound > maxProfit:
            q.put(v)

    return maxProfit

W = 10
arr = [Item(2, 40), Item(3.14, 50), Item(1.98, 100), Item(5, 95), Item(3, 30)]
n = len(arr)

print('Maximum possible profit =', knapsack_solution(W, arr, n))
