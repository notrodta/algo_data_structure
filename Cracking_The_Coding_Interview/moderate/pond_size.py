# Pond Sizes: You have an integer matrix representing a plot of land, where the value at that loca­ tion represents the height above sea level. A value of zero indicates water. A pond is a region of water connected vertically, horizontally, or diagonally. The size of the pond is the total number of connected water cells. Write a method to compute the sizes of all ponds in the matrix.

# EXAMPLE
# Input:
# 0210
# 0101
# 1101
# 0101
# Output: 2, 4, 1 (in any order)


pond = [
    [0,2,1,0],
    [0,1,0,1],
    [1,1,0,1],
    [0,1,0,1],
]


def ans(pond):
    l = set()

    pond_node_visited = set()

    for r in range (0, len(pond)):
        for c in range(0, len(pond[r])):
            if (r,c) not in pond_node_visited and pond[r][c] == 0:
                #print(r,c, "pond node:", pond[r][c])
                sum = bfs(pond, r, c, pond_node_visited)
                #print("---- new ----")
                l.add(sum)
    return l


def get_neighbor(pond, r, c):
    l = []

    pond_len = len(pond)

    # bottom
    if r+1 < pond_len:
        l.append((r+1,c))
        if c - 1 > 0: # bottom left
            l.append((r+1,c-1))
        if c + 1 < len(pond[r]): # bottom right
            l.append((r+1, c+1))

    # top
    if r-1 >= 0:
        l.append((r-1,c))
        if c - 1 > 0: # top left
            l.append((r-1, c-1))
        if c + 1 < len(pond[r]): # top right
            l.append((r-1, c+1))


    # right
    if c + 1 < len(pond[r]):
        l.append((r, c+1))

    # left
    if c - 1 > 0:
        l.append((r,c-1))

    return l






from collections import deque
def bfs(pond,r,c,pond_node_visited):
    q = deque([])
    visited = set()
    q.append( (r,c) )
    visited.add((r,c))

    sum = 1

    # 'n' needs fixing
    while q:
        curr = q.popleft()
        #print(get_neighbor(pond, curr[0], curr[1]))
        for n in get_neighbor(pond, curr[0],curr[1]):
            n_r = n[0]
            n_c = n[1]
            if n not in visited and pond[n_r][n_c] == 0:
                visited.add(n)
                pond_node_visited.add( (n_r, n_c) )
                q.append( (n_r, n_c) )
                sum += 1
                #print("extend at:", n_r, n_c, ",new pond node:", pond[n_r][n_c], ",curr sum", sum)

    #print("sum", sum)
    return sum


print(ans(pond))



