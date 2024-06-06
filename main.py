from openai import OpenAI
import os
from src.book import *
from json import loads

from src.writer import Writer


writer = Writer()

basic_info = loads(writer.generate_book_summary("A book about parenting kids with ADHD."))

print(basic_info['title'])
print(basic_info['summary'])

