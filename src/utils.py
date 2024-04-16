def print_matrix(matrix, rows_index, columns_index):
    print(' ', ' '.join(map(str, columns_index)))
    for i, row in enumerate(matrix):
        print(rows_index[i], ' '.join(map(str, row)))