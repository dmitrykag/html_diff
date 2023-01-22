def lines_diff(lines1, lines2):
        matrix = [[None]*(len(lines2) + 1) for i in range(len(lines1) + 1)]
        for i in range(len(matrix[0])):
            matrix[0][i] = (i, -1, -1)
        
        for i in range(len(matrix)):
            matrix[i][0] = (i, -1, -1)

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                del_element = (matrix[i - 1][j][0] + 1, i - 1, j)
                ins_element = (matrix[i][j-1][0] + 1, i, j - 1)
                replace_cost = matrix[i-1][j-1][0]
                if lines1[i-1] != lines2[j-1]:
                    replace_cost += 1
                replace_element = (replace_cost, i - 1, j - 1)
                el = replace_element
                if el[0] > del_element[0]:
                    el = del_element
                if el[0] > ins_element[0]:
                    el = ins_element

                matrix[i][j] = el

        el = matrix[-1][-1]
        path = [(len(matrix)-2, len(matrix[0])-2)]
        while el[1] != -1:
            path.append((el[1]-1,el[2]-1))
            el = matrix[el[1]][el[2]]

        return path[::-1], matrix[-1][-1][0]

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

if __name__ != "main":
    diff, cost = lines_diff("horse", "ros")
    print(diff, cost)
    explain("horse", "ros", diff)
    diff, cost = lines_diff("intention", "execution")
    print(diff, cost)
    explain("intention", "execution", diff)

