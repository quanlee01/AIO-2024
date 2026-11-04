def levenshtein_distance(s1, s2):
    rows, cols = len(s1) + 1, len(s2) + 1
    matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        matrix[i][0] = i
    for j in range(cols):
        matrix[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):
            cost = s1[i - 1] != s2[j - 1]
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + cost,
            )

    return matrix[-1][-1]


print(levenshtein_distance("hello", "halo"))