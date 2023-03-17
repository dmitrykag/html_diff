class Coord:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __repr__(self):
        return str((self.i, self.j))

class MatrixElement:
    def __init__(self, cost: int, coord: Coord):
        self.cost = cost
        self.coord = coord


def get_matrix(word1, word2):
    matrix = [[0]*(len(word2) + 1) for i in range(len(word1) + 1)]
    
    for j in range(len(matrix[0])):
        matrix[0][j] = MatrixElement(j, Coord(0, j - 1))
    
    for i in range(len(matrix)):
        matrix[i][0] = MatrixElement(i, Coord(i - 1, 0))

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            del_el = MatrixElement(matrix[i - 1][j].cost + 1, Coord(i - 1, j))
            ins_el = MatrixElement(matrix[i][j-1].cost + 1, Coord(i, j - 1))
            
            replace_cost = matrix[i-1][j-1].cost
            if word1[i-1] != word2[j-1]:
                replace_cost += 1

            replace_el = MatrixElement(replace_cost, Coord(i - 1, j - 1))

            matrix[i][j] = min(del_el, ins_el, replace_el, key=lambda x: x.cost)

    return matrix

def edit_sequence(word1, word2):
    matrix = get_matrix(word1, word2)

    result = []
    m = matrix[-1][-1]
    begin = m.coord
    end = Coord(len(word1), len(word2))
    while begin.i != -1 and begin.j != -1:
        if begin.i == end.i:
            result.append(Coord(-1, begin.j))
        elif begin.j == end.j:
            result.append(Coord(begin.i, -1))
        else:
            result.append(begin)
        m = matrix[begin.i][begin.j]
        end = begin
        begin = m.coord

    return result[::-1]


if __name__ == "__main__":
    print(edit_sequence("abcd", "abd"))
