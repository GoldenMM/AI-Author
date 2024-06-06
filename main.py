from src.book import *
from src.writer import Writer



book = Book("Parenting kids with ADHD")

for chapter in book.chapters:
    print(book.chapters[chapter])

