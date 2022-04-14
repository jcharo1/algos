
""""# Problem Statement

Find and return the `nth` row of Pascal's triangle in the form a list. `n` is 0-based.

For example, if `n = 4`, then `output = [1, 4, 6, 4, 1]`.

To know more about Pascal's triangle: https://www.mathsisfun.com/pascals-triangle.html

"""




def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    row = 11 ** n
    output = [int(x) for x in str(row)]
    return print(output)

nth_row_pascal(4)
