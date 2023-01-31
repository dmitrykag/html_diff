
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import edit_sequence

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


def get_html(first, second):
    header = '<html><head></head><body><table border="1" style="border-collapse:collapse";>\n'
    footer = '</table></body></html>'

    lines1 = first.splitlines()
    lines2 = second.splitlines()

    diff = edit_sequence.edit_sequence(lines1, lines2)

    content = ''
    for edit in diff:
        row = '<tr>'
        if edit[0] == -1:
            cells = '<td /><td>' + lines2[edit[1]] + '</td>'
            row = '<tr bgcolor="LightBlue">'
        elif edit[1] == -1:
            cells = '<td>' + lines1[edit[0]] + '</td><td />'
            row = '<tr bgcolor="LightBlue">'
        else:
            if lines1[edit[0]] != lines2[edit[1]]:
                row = '<tr bgcolor="pink">'
        
            cells = '<td>' + lines1[edit[0]] + '</td>'
            cells += '<td>' + lines2[edit[1]] + '</td>'

        content += row + cells + '</tr>\n'

    return header + content + footer

if __name__ == "__main__":
    app.run()