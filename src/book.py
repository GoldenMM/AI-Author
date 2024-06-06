from src.writer import Writer
from json import loads
        
class Section():
    def __init__(self, title, summary, chapter):
        self.title = title
        self.summary = summary
        self.chapter = chapter
        self.edited = False
        
        
        self.content = None
        
        
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
        self.edited = False
    
    #TODO: Implement this method when writer is ready    
    def split_section(self, section: Section):
        '''Used when token limit is exceeded and the section needs to be split inplace.'''
        pass
    
    def __repr__(self) -> str:
        return f"{self.title}"
        
class Book():
    '''A class representing a book and its contents. The constructor builds the book's contents from a prompt'''
    def __init__(self, prompt: str):
        self.writer = Writer()
        self.edited = False
        
        # Generate title and summary
        print("Generating title and summary...")
        title_and_summary = loads(self.writer.generate_book_summary(prompt))
        self.title = title_and_summary['title']
        self.summary = title_and_summary['summary']
        print("Title and summary generated.")
        
        #Generate table of contents and chapter summaries
        print("Generating table of contents and chapter summaries...")
        self.toc = loads(self.writer.generate_toc(self.title, self.summary))
        self.chapters = {}  # chapter number: Chapter object
        for chapter in self.toc:
            self.chapters[chapter] = Chapter(self.toc[chapter]['chapter_title'], self.toc[chapter]['summary'])
        print("Table of contents and chapter summaries generated.")
    
    #TODO: Implement this method when book generation is done
    def parse(self):
        '''Parses the book's contents for saving.'''
        pass
        