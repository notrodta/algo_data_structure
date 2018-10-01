# Paint Fill: Implement the "paint fill" function that one might see on many image editing programs. That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color, fill in the surrounding area until the color changes from the original color.


def paintfill(matrix, r, c, oldcolor, newcolor):
    if r < 0 or r > len(matrix) or c < 0 or c > len(matrix[0]): return
    if matrix[r][c] == newcolor: return
    if matrix[r][c] == oldcolor: matrix[r][c] = newcolor

    paintfill(matrix, r+1, c, oldcolor, newcolor)
    paintfill(matrix, r-1, c, oldcolor, newcolor)
    paintfill(matrix, r, c-1, oldcolor, newcolor)
    paintfill(matrix, r, c+1, oldcolor, newcolor)