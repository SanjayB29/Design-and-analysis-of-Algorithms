import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    min_pair = None
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                min_pair = (points[i], points[j])
    return min_pair

def closest_split_pair(px, py, delta, best_pair):
    ln_x = len(px)
    midpoint = px[ln_x // 2][0]
    sy = [p for p in py if midpoint - delta <= p[0] <= midpoint + delta]
    best = delta
    ln_y = len(sy)
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = sy[i], sy[j]
            dist = distance(p, q)
            if dist < best:
                best_pair = p, q
                best = dist
    return best_pair

def closest_pair_rec(px, py):
    if len(px) <= 3:
        return brute_force(px)
    mid = len(px) // 2
    qx = px[:mid]
    rx = px[mid:]

    midpoint = px[mid][0]
    qy = list(filter(lambda x: x[0] <= midpoint, py))
    ry = list(filter(lambda x: x[0] > midpoint, py))

    left_pair = closest_pair_rec(qx, qy)
    right_pair = closest_pair_rec(rx, ry)
    min_pair = left_pair if distance(*left_pair) < distance(*right_pair) else right_pair

    return closest_split_pair(px, py, distance(*min_pair), min_pair)

def closest_pair(points):
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair_rec(px, py)

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (6,1), (12, 10), (3, 4)]
result = closest_pair(points)
print("The closest pair of points is:", result)


