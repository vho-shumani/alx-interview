def pascal_triangle(n):
    triangle_list = []
    if n <= 0:
        return triangle_list
    
    for i in range(n):
        row_list = [1] * (i + 1)
        for j in range(1, i):
            row_list[j] = triangle_list[i - 1][j - 1] + triangle_list[i - 1][j]
        triangle_list.append(row_list)
    return triangle_list

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))