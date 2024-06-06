from src.writer import Writer
        
class Section():
    def __init__(self, title, summary):
        self.title = title
        self.content = None
        self.summary = summary
        
    def __repr__(self):
        return self.title
    
    #TODO: Implement this method when writer is ready  
    def split(self):
        '''Splits the content of the section into two parts.'''
        pass

        
class Chapter():
    def __init__(self, title: str):
        self.title = title
        self.sections = []
        self.summary = None
        
    def add_section_tail(self, section: Section):
        self.content.append(section)
    
    #TODO: Implement this method when writer is ready    
    def split_section(self, section: Section):
        '''Used when token limit is exceeded and the section needs to be split inplace.'''
        pass
        
class Book():
    def __init__(self):
        self.title = None
        self.chapters = {}  # chapter number: Chapter object
        self.summary = None
        self.writer = Writer()

    def __repr__(self) -> str:
        return f'''|{self.title}|
        ------------------------- 
        {self.chapters["TOC"]}'''