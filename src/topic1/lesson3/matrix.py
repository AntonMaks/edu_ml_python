if __name__ == '__main__':
    M1 = [[1, 2, 3, 4, 11],
          [5, -6, 7, 8, 11],
          [5, 2, -42, 8, 11],
          [1, 6, 7, 11, 100]]

    # print ALL elements of matrix
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            print(M1[i][j])
    print("==============")

    M2 = [[1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]

    # print diagonal - 1,-6,5,11
    index = 0
    for i in range(len(M2[index])):
        print(M2[i][index])
        index += 1
    print("==============")

    M3 = [[1, 2, 3, 4],
          [5, 2, 7, 8],
          [5, 6, 3, 8],
          [1, 6, 7, 4]]

    # print diagonal in opposite order  4, 3, 2, 1
    index_M3 = (len(M3) - 1)
    while index_M3 >= 0:
        print(M3[index_M3][index_M3])
        index_M3 -= 1
