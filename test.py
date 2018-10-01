#image matching:
# count how many regions are matching between 2 matrices
# a region is active if tehre is a 1

'''

ex:
grid1:
111
100
100

grid2:
111
100
101

only 1 matching region starting at (0,0)



'''


# Complete the countMatches function below.
def get_regions(grid, r, c, region):

    if r >= len(grid) or r < 0 or c >= len(grid) or c < 0:
        return

    if grid[r][c] == '0':
        return

    if (r, c) in region:
        return

    if grid[r][c] == '1':
        region.append((r, c))

    get_regions(grid, r + 1, c, region)
    get_regions(grid, r - 1, c, region)
    get_regions(grid, r, c + 1, region)
    get_regions(grid, r, c - 1, region)


def get_all_region_for_grid(grid):
    region = set()
    new_add = True
    for r in range(0, len(grid)):
        for c in range(0, len(grid[r])):
            if grid[r][c] == '1':
                if len(region) > 0:
                    new_add = True
                    for lst in region:
                        if (r, c) in lst:
                            new_add = False

                    if new_add:
                        l = []
                        get_regions(grid, r, c, l)
                        l = tuple(l)
                        region.add(l)
                else:
                    l = []
                    get_regions(grid, r, c, l)
                    l = tuple(l)
                    region.add(l)

    return region


def get_long_and_short_grid(grid1, grid2):
    if len(grid1) > len(grid2):
        long_grid = grid1
        short_grid = grid2
    else:
        long_grid = grid1
        short_grid = grid2

    return long_grid, short_grid


def countMatches(grid1, grid2):
    grid1_region = get_all_region_for_grid(grid1)
    grid2_region = get_all_region_for_grid(grid2)

    matching_regions = 0

    long_grid, short_grid = get_long_and_short_grid(grid1_region, grid2_region)

    for e1 in long_grid:
        if e1 in short_grid:
            matching_regions += 1

    return matching_regions



g1 = [['0','0','1'], ['0','1','1'], ['1','0','1']]
g2 = [['0','0','1'], ['0','1','1'], ['1','0','1']]
print(countMatches(g1,g2))




# orignial submitted to twitter: did not hash it, used only list
# # Complete the countMatches function below.
# def get_regions(grid, r, c, region):
#     # print("r,c", r,c)
#     if r >= len(grid) or r < 0 or c >= len(grid) or c < 0:
#         # print("out of grid")
#         return
#
#     # print("curr: ", grid[r][c])
#
#     if grid[r][c] == '0':
#         # print("not matching region")
#         return
#
#     if [r, c] in region:
#         # print("already found")
#         return
#
#     if grid[r][c] == '1':
#         # print("adding: ", [r,c])
#         region.append([r, c])
#
#     # print(region)
#     # print()
#
#     # print("r+1")
#     get_regions(grid, r + 1, c, region)
#     # print("r-1")
#     get_regions(grid, r - 1, c, region)
#     # print("c+1")
#     get_regions(grid, r, c + 1, region)
#     # print("c-1")
#     get_regions(grid, r, c - 1, region)
#
#
# def get_all_region_for_grid(grid):
#     region = []
#     new_add = True
#     for r in range(0, len(grid)):
#         for c in range(0, len(grid[r])):
#             # print("asdasdasd:",r,c)
#             if grid[r][c] == '1':
#                 if len(region) > 0:
#                     new_add = True
#                     # print()
#                     # print("curr region:", region)
#                     for lst in region:
#                         # print("region lst: ", lst)
#                         if [r, c] in lst:
#                             new_add = False
#
#                     if new_add:
#                         # print("NEW CALL!: ", r,c)
#                         l = []
#                         get_regions(grid, r, c, l)
#                         region.append(l)
#                 else:
#                     # print("inital call!: ", r,c)
#                     # print()
#                     l = []
#                     get_regions(grid, r, c, l)
#                     # print("l",l)
#                     region.append(l)
#
#     # get_regions(grid1,0,2, region)
#     return region
#
#
# def get_long_and_short_grid(grid1, grid2):
#     if len(grid1) > len(grid2):
#         long_grid = grid1
#         short_grid = grid2
#     else:
#         long_grid = grid1
#         short_grid = grid2
#
#     return long_grid, short_grid
#
#
# def countMatches(grid1, grid2):
#     grid1_region = get_all_region_for_grid(grid1)
#     grid2_region = get_all_region_for_grid(grid2)
#
#     print(grid1_region)
#     print(grid2_region)
#     print()
#
#     matching_regions = 0
#
#     long_grid, short_grid = get_long_and_short_grid(grid1_region, grid2_region)
#     long_grid_len = len(long_grid)
#
#     # if current list in grid1_region and grid2_region are hte same length:
#     # compare the inside elements to see everything is also the same
#     # else: different
#
#     all_matching = False
#     continue_iterating = True
#     for e1 in long_grid:
#         continue_iterating = True
#         if continue_iterating:
#             for e2 in short_grid:
#                 if len(e1) == len(e2):
#                     print("e1:", e1, "e2:", e2)
#                     for element in e1:
#                         # print("element: ", element)
#                         if element in e2:
#                             all_matching = True
#                             continue_iterating = False
#                         else:
#                             all_matching = False
#                             break
#
#                     if all_matching:
#                         matching_regions += 1
#                     print("matching_regions: ", matching_regions)
#                     print()
#                     all_matching = False
#
#     return matching_regions
#     # return grid1_region, grid2_region
#
#
# g1 = [['0','0','1'], ['0','1','1'], ['1','0','0']]
# g2 = [['0','0','1'], ['0','1','1'], ['1','0','1']]
# print(countMatches(g1,g2))




#Q2
'''
input: reversed ascii string

output: get the actual string by inverting the reversed ascii string

'''


# Complete the decode function below.
def get_reversed_ascii(num):
    s = ""
    for i in reversed(num):
        s = s + i
    return s


def get_ascii_list():
    available_ascii = set()
    for i in range(65, 91):
        available_ascii.add(str(i))
    for i in range(97, 123):
        available_ascii.add(str(i))
    available_ascii.add(str(32))

    return available_ascii


def decode(encoded):
    available_ascii = get_ascii_list()
    encoded_reversed = get_reversed_ascii(encoded)
    encoded_reversed_len = len(encoded_reversed)

    my_ascii_list = ""

    i = 0
    while i < encoded_reversed_len:
        num1 = encoded_reversed[i:i + 2]
        num2 = encoded_reversed[i:i + 3]
        if num1 in available_ascii:
            my_ascii_list = my_ascii_list + (chr(int(num1)))
            i = i + 2
        else:
            my_ascii_list = my_ascii_list + (chr(int(num2)))
            i = i + 3

    return my_ascii_list



