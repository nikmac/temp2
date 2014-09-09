import csv
import webbrowser


class Element(object):
    def __init__(self, id, type, parent, text):
        self.id = id
        self.type = type
        self.parent = parent
        self.text = text

class Div(Element):
    def __init__(self, id, type, parent, text):
        super(Div, self).__init__(id=id, type=type, parent=parent, text=text)
        html = "<div id=" + id + ">" + text + "</div>"
        printer(html)


class H2(Element):
    def __init__(self, id, type, parent, text):
        super(H2, self).__init__(id=id, type=type, parent=parent, text=text)
        html = "<h2 id=" + id + ">" + text + "</h2>"
        printer(html)


class H3(Element):
    def __init__(self, id, type, parent, text):
        super(H3, self).__init__(id=id, type=type, parent=parent, text=text)
        html = "<h3 id=" + id + ">" + text + "</h3>"
        printer(html)


class P(Element):
    def __init__(self, id, type, parent, text):
        super(P, self).__init__(id=id, type=type, parent=parent, text=text)
        html = "<p id=" + id + ">" + text + "</p>"
        printer(html)


class Span(Element):
    def __init__(self, id, type, parent, text):
        super(Span, self).__init__(id=id, type=type, parent=parent, text=text)
        html = "<span id=" + id + ">" + text + "</span>"
        printer(html)


def printer(html):
    with open('parse.html', 'a') as write_file:
        write_file.write(html)


def csv_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        if line["type"] == "div":
            div = Div(line["id"], line["type"], line["parent"], line["text"])
        if line["type"] == "h2":
            h2 = H2(line["id"], line["type"], line["parent"], line["text"])
        if line["type"] == "h3":
            h3 = H3(line["id"], line["type"], line["parent"], line["text"])
        if line["type"] == "p":
            p = P(line["id"], line["type"], line["parent"], line["text"])
        if line["type"] == "span":
            span = Span(line["id"], line["type"], line["parent"], line["text"])


def open_html():
    header = """<html>
    <head>
    </head>
    <body>"""
    footer = """</body>
    </html>"""
    with open('parse.html', 'w') as write_file:
        write_file.write(header)
    with open('html.csv', 'rb') as file:
        csv_reader(file)
    file.close()
    with open('parse.html', 'a') as write_file:
        write_file.write(footer)


open_html()
filename = 'file:///Users/niki/week2/parse.html'
webbrowser.open_new_tab(filename)



