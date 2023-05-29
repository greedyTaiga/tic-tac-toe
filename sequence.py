def mirror_y(matrix):
    return [row[::-1] for row in matrix]

def turn90(matrix):
    res = []
    for i in range(len(matrix)):
       res.append([row[i] for row in matrix])
    return res

def check_sub_in_matrix(matrix, s):
    res = False
    for row in matrix:
        res = res or check_sub_in_list(row, s)
    return res

def check_sub_in_list(l, s):
    for i in range(len(l) - len(s) + 1):
        if l[i:i+len(s)] == s:
            return True
    return False

def check_sub_in_diag(matrix, s):
    for i in range(len(matrix) - len(s) + 1):
        for j in range(len(matrix[i]) - len(s) + 1):
            seq = []
            for k in range(len(s)):
                seq.append(matrix[i + k][j + k])
            if seq == s:
                return True
    return False
