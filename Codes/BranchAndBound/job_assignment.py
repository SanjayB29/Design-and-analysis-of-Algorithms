from queue import PriorityQueue

class Node:
    def __init__(self, path, level, cost, workerID, n):
        # Stores the solution up to this point
        self.path = path
        # Stores the number of assigned jobs
        self.level = level
        # Stores the total cost up to this point
        self.cost = cost
        # Stores the worker ID
        self.workerID = workerID
        # Total number of jobs
        self.n = n

    def __lt__(self, nxt):
        return self.cost < nxt.cost

def jobAssignment(costMatrix):
    n = len(costMatrix)
    # Min heap to store the nodes of search tree
    pq = PriorityQueue()
    # Start with a dummy node at level 0 - no job is assigned
    start = Node([-1]*n, 0, 0, -1, n)
    pq.put(start)
    
    minCost = float('inf')
    pruning_count = 0
    final_path = []

    while not pq.empty():
        # Get the minimum cost node from the priority queue
        curNode = pq.get()
        
        # If all jobs are assigned
        if curNode.level == n:
            minCost = curNode.cost
            final_path = curNode.path
            break

        for j in range(n):
            if j not in curNode.path:
                nextPath = curNode.path[:]
                nextPath[curNode.level] = j

                nextCost = curNode.cost + costMatrix[curNode.level][j]

                if nextCost < minCost:
                    nextNode = Node(nextPath, curNode.level + 1, nextCost, j, n)
                    pq.put(nextNode)
                else:
                    pruning_count += 1

    print(f"Minimum cost: {minCost}")
    print(f"Job assignment: {final_path}")
    print(f"Total prunings done: {pruning_count}")

# Example
costMatrix = [[9, 2, 7, 8],
              [6, 4, 3, 7],
              [5, 8, 1, 8],
              [7, 6, 9, 4]]

jobAssignment(costMatrix)
