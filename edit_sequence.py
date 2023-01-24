def replace_cost(sequence1, sequence2, index1, index2):
    len1, len2 = len(sequence1[index1]), len(sequence2[index2])
    if sequence1[index1] == sequence2[index2]:
        return 0
    elif abs(index1 - index2) > 5 or abs(len1 - len2) > (len1 + len2) / 5:
        return len(sequence1[index1]) + len(sequence2[index2])
    elif len(sequence1) == len(sequence2) == 1:
        return 1
    else:
        return edit_distance(sequence1[index1], sequence2[index2])



def diff_matrix(sequence1, sequence2):
        matrix = [[None]*(len(sequence2) + 1) for i in range(len(sequence1) + 1)]
        for i in range(len(matrix[0])):
            matrix[0][i] = (i, -1, -1)
        
        for i in range(len(matrix)):
            matrix[i][0] = (i, -1, -1)

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                del_element = (matrix[i - 1][j][0] + len(sequence1[i-1]), i - 1, j)
                ins_element = (matrix[i][j-1][0] + len(sequence2[j-1]), i, j - 1)
                cost = replace_cost(sequence1, sequence2, i - 1, j - 1)
                replace_element = (matrix[i-1][j-1][0] + cost, i - 1, j - 1)
                el = replace_element
                if el[0] > del_element[0]:
                    el = del_element
                if el[0] > ins_element[0]:
                    el = ins_element

                matrix[i][j] = el

        return matrix

def edit_distance(sequence1, sequence2):
        matrix = diff_matrix(sequence1, sequence2)
        return matrix[-1][-1][0]

def edit_sequence(sequence1, sequence2):
        matrix = diff_matrix(sequence1, sequence2)

        el = matrix[-1][-1]
        path = [(len(matrix)-1, len(matrix[0])-1)]
        while el[1] != -1:
            path.append((el[1],el[2]))
            el = matrix[el[1]][el[2]]

        return [(coord1 - 1, coord2 - 1) for (coord1, coord2) in reversed(path)]

def explain(lines1, lines2, diff):
    prev = diff[0]
    for i in range(1, len(diff)):
        if diff[i][0] == prev[0]:
            print('insert ' + lines2[diff[i][1]])
        elif diff[i][1] == prev[1]:
            print('remove ' + lines1[diff[i][0]])
        else:
            print('replace ' + lines1[diff[i][0]] + ' with ' + lines2[diff[i][1]])
        prev = diff[i]

if __name__ == "main":
    diff = edit_sequence("horse", "ros")
    print(diff)
    explain("horse", "ros", diff)
    diff = edit_sequence("intention", "execution")
    print(diff)
    explain("intention", "execution", diff)

