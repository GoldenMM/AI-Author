from __future__ import annotations
from src.writer import Writer
from json import loads

        
class Section():
    def __init__(self, title: str, summary: str, chapter: Chapter):
        self.title = title
        self.summary = summary
        self.chapter = chapter
        self.edited = False
        
        print(f"Generating content for section {self.title}...")
        self.content = self.chapter.book.writer.generate_section_content(self.title,
                                                                         self.summary,
                                                                         self.chapter.summary,
                                                                         self.chapter.sections)
        print(f"Content for section {self.title} generated.\n")
        
        
    def __repr__(self):
        return f"{self.content}"
    
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
        sections_temp = loads(self.book.writer.generate_chapter_sections(self.title, self.summary))
        for section in sections_temp:
            self.sections[section] = Section(sections_temp[section]['title'], sections_temp[section]['summary'], self)
        print(f"Sections for chapter {self.title} generated. \n")
    
    #TODO: Implement this method when writer is ready    
    def split_section(self, section: Section):
        '''Used when token limit is exceeded and the section needs to be split inplace.'''
        pass
    
    def __repr__(self) -> str:
        ret = f"## {self.title}\n"
        for section in self.sections:
            ret += f"{self.sections[section].content}\n\n"
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
        print("Title and summary generated.\n")
        
        #Generate table of contents and chapter summaries
        print("Generating table of contents and chapter summaries...")
        self.toc = loads(self.writer.generate_toc(self.title, self.summary))
        self.chapters = {}  # chapter number: Chapter object
        for chapter in self.toc:
            self.chapters[chapter] = Chapter(self.toc[chapter]['chapter_title'], self.toc[chapter]['summary'], self)
        print("Table of contents and chapter summaries generated.\n")
    
    #TODO: Implement this method when book generation is done
    def parse(self):
        '''Parses the book's contents for saving.'''
        pass
    
    def __repr__(self) -> str:
        ret = f"# {self.title}\n{self.summary}\n\n"
        for chapter in self.chapters:
            ret += f"{self.chapters[chapter]}\n\n"
        return ret
        