from src.writer import Writer
from json import loads
        
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
    def __init__(self, title: str, summary: str):
        self.title = title
        self.summary = summary
        self.sections = []
         
    def add_section_tail(self, section: Section):
        self.content.append(section)
    
    #TODO: Implement this method when writer is ready    
    def split_section(self, section: Section):
        '''Used when token limit is exceeded and the section needs to be split inplace.'''
        pass
    
    def __repr__(self) -> str:
        return f"{self.title}"
        
class Book():
    def __init__(self, prompt: str):
        self.writer = Writer()
        
        # Generate title and summary
        title_and_summary = loads(self.writer.generate_book_summary(prompt))
        self.title = title_and_summary['title']
        self.summary = title_and_summary['summary']
        
        self.toc = loads(self.writer.generate_toc(self.title, self.summary))
        
        self.chapters = {}  # chapter number: Chapter object
        for chapter in self.toc:
            self.chapters[chapter] = Chapter(self.toc[chapter]['chapter_title'], self.toc[chapter]['summary'])

    def __repr__(self) -> str:
        return f'''|{self.title}|
        ------------------------- 
        {self.chapters["TOC"]}'''