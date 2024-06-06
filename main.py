from openai import OpenAI
import os
from src.book import *
from json import loads
import tiktoken
from src.writer import Writer



book = Book("Parenting kids with ADHD")

for chapter in book.chapters:
    print(book.chapters[chapter])

