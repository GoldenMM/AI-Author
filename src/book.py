from src.writer import Writer
from json import loads
from __future__ import annotations
        
class Section():
    def __init__(self, title: str, summary: str, chapter: Chapter):
        self.title = title
        self.summary = summary
        self.chapter = chapter
        self.edited = False
        
        
        self.content = self.chapter.book.writer.generate_section_content(self.title,
                                                                         self.summary,
                                                                         self.chapter.summary,
                                                                         self.chapter.sections)
        
        
    def __repr__(self):
        return f"###{self.title}\n{self.content}"
    
    #TODO: Implement this method when writer is ready  
    def split(self):
        '''Splits the content of the section into two parts.'''
        pass

        
class Chapter():
    def __init__(self, title: str, summary: str, book: Book):
        self.book = book
        self.title = title
        self.summary = summary
        self.edited = False
        
        # Generate sections
        print(f"Generating sections for chapter {self.title}...")
        self.sections = {}
        for section in loads(self.book.writer.generate_chapter_sections(self.title, self.summary)):
            print(f"Generating section {section['title']}...")
            self.sections[section] = Section(section['title'], section['summary'], self)
            print(f"Section {section['title']} generated.")
        print(f"Sections for chapter {self.title} generated.")
    
    #TODO: Implement this method when writer is ready    
    def split_section(self, section: Section):
        '''Used when token limit is exceeded and the section needs to be split inplace.'''
        pass
    
    def __repr__(self) -> str:
        ret = f"##{self.title}\n"
        for section in self.sections:
            ret += f"{self.sections[section]}\n\n"
        return ret
        
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
    
    def __repr__(self) -> str:
        ret = f"#{self.title}\n{self.summary}\n\n"
        
        
        for chapter in self.chapters:
            ret += f"{self.chapters[chapter]}\n\n"
        return ret
        