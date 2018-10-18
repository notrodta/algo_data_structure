 # 16.3 Intersection: Given two straight line segments (represented as a start point and an end point), compute the point of intersection, if any.

# get m form point slop formula
def slope(x1, x2, y1, y2):
    return (y2 - y1) / (x2 - x1)

 # get b from y = mx+b
def get_b(x,y, m):
    return y - (x*m)

# https://www.youtube.com/watch?v=UlexMTWrkxI
def answer(p1_start, p1_end, p2_start, p2_end):
    p1_x1 = p1_start[0]
    p1_y1 = p1_start[1]
    p1_x2 = p1_end[0]
    p1_y2 = p1_end[1]

    p2_x1 = p2_start[0]
    p2_y1 = p2_start[1]
    p2_x2 = p2_end[0]
    p2_y2 = p2_end[1]

    slope1 = slope(p1_x1, p1_x2, p1_y1, p1_y2)
    slope2 = slope(p2_x1, p2_x2, p2_y1, p2_y2)

    b1 = get_b(p1_x1, p1_y1, slope1)
    b2 = get_b(p2_x1, p2_y1, slope2)

    x = (b1-b2) / (slope2 - slope1)

    return x, slope1 * x + b1


p1_start = (1,2)
p1_end = (4,5)
p2_start = (1,5)
p2_end = (4,2)
print(answer(p1_start, p1_end, p2_start, p2_end))


p1_start = (1,1)
p1_end = (4,4)
p2_start = (1,8)
p2_end = (2,4)
print(answer(p1_start, p1_end, p2_start, p2_end))