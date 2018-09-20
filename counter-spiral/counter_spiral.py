def counterClockspiralPrint(arr):
    k = 0
    l = 0

    # k - starting row index
    # m - ending row index
    # l - starting column index
    # n - ending column index
    # i - iterator

    # initialize the count
    cnt = 0

    # total number of
    # elements in matrix
    m = len(arr)
    n = len(arr)
    total = m * n

    while (k < m and l < n):
        if (cnt == total):
            break

        # Print the first column
        # from the remaining columns
        for i in range(k, m):
            print(arr[i][l], end=" ")
            cnt += 1

        l += 1

        if (cnt == total):
            break

        # Print the last row from
        # the remaining rows
        for i in range(l, n):
            print(arr[m - 1][i], end=" ")
            cnt += 1

        m -= 1

        if (cnt == total):
            break

        # Print the last column
        # from the remaining columns
        if (k < m):
            for i in range(m - 1, k - 1, -1):
                print(arr[i][n - 1], end=" ")
                cnt += 1
            n -= 1

        if (cnt == total):
            break

        # Print the first row
        # from the remaining rows
        if (l < n):
            for i in range(n - 1, l - 1, -1):
                print(arr[k][i], end=" ")
                cnt += 1

            k += 1

# Form matrix


def formMatrix(n):
    temp = []
    for i in range(n):
        l = list(map(int, input().split(' ')))
        temp.append(l)
    return temp


n = int(input())
matrix = formMatrix(n)
counterClockspiralPrint(matrix)
