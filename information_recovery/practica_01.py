from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attrs):
        if self.recording:
            self.recording += 1
            return
        else:
            self.recording = 1
            return


    def handle_endtag(self, tag):
        self.recording -= 1

    def handle_data(self, data):
        print("depth: " + str(self.recording) + data)

parser = MyHTMLParser()
with open("practica_01_documents.xml", 'r', encoding='utf8') as myfile:
    data=myfile.read().replace('\n', '')

parser.feed(data)