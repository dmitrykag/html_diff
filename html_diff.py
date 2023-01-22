
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('test.html') as htm:
        return htm.read()


@app.route('/show_file', methods = ['POST'])
def show_file():
    left = request.files.get('first_file')
    right = request.files.get('second_file')
    cont1 = left.read()
    cont2 = right.read()
    return get_html(cont1.decode('utf-8'), cont2.decode('utf-8'))

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


def get_html(first, second):
    header = '<html><head></head><body><table border="1" style="border-collapse:collapse";>\n'
    footer = '</table></body></html>'

    lines1 = first.split('\n')
    lines2 = second.split('\n')

    diff, cost = lines_diff(lines1, lines2)

    content = ''
    prev = diff[0]
    for i in range(1, len(diff)):
        row = '<tr>'
        if diff[i][0] == prev[0]:
            cells = '<td /><td>' + lines2[diff[i][1]] + '</td>'
        elif diff[i][1] == prev[1]:
            cells = '<td>' + lines1[diff[i][0]] + '</td><td />'
        else:
            if lines1[diff[i][0]] != lines2[diff[i][1]]:            
                row = '<tr bgcolor="pink">'
        
            cells = '<td>' + lines1[diff[i][0]] + '</td>'
            cells += '<td>' + lines2[diff[i][1]] + '</td>'

        content += row + cells + '</tr>\n'
        prev = diff[i]

    return header + content + footer

if __name__ == "__main__":
    app.run()