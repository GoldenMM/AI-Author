from src.book import *
from src.writer import Writer
import os



# book = Book("Parenting kids with ADHD")

with open("book.md", "r") as f:
    print(len(f.read().split(" ")))


