


class Book():
    def __init__(self):
        self.title = None
        self.table_of_contents = None
        self.chapters = []
        self.summary = None

class Chapter():
    def __init__(self):
        self.title = None
        self.subchapters = []
        self.summary = None
        
class Subchapter():
    def __init__(self, title, summary):
        self.title = title
        self.content = None
        self.summary = summary