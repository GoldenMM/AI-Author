from openai import OpenAI
import os
import tiktoken

class Writer():
    '''Class for generating text using OpenAI's GPT-3.5-turbo model. Contains and OpenAI client on initialization.
    Has methods for generating text based on prompts or existing Book data.'''
    def __init__(self):
        print("Initializing Writer...")
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )
        self.encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    
    def generate_text(self, prompt) -> str:
        '''Basic text generation using GPT-3.5-turbo model.
        Will be depreciated in favour of more specific methods.'''
        chat_completion = self.client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content
    
    def generate_book_summary(self, prompt: str) -> str:
        '''Generates a summary and title of the book.'''
        chat_completion = self.client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f'''You are an expert writer and you have been asked to begin the first steps of writing a book.
                            The high level idea of the book is the following:
                            "{prompt}".
                            You are to generate a title for the book and a summary of the book's ideas and the points it will make.
                            Reply in the following json format:
                            {{
                                "title: "<title>",
                                "summary": "<summary>
                            }}"'''
            }
        ],
        model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content
    
    def generate_toc(self, title: str, summary: str) -> str:
        '''Generates a table of contents and chapter summaries for the book.'''
        chat_completion = self.client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f'''You are an expert writer and you have been asked to begin the first steps of writing a book.
                            You have the book's title as "{title}" and the book's summary as "{summary}".
                            You are to generate a table of contents for the book based on the title and summary.
                            Reply in the following json format for as many chapters as you see fit:
                            {{
                                "<chapter_number>": {{
                                    "chapter_title": "<chapter_title>",
                                    "summary": "<chapter_summary>"
                                }},
                                ...
                            }}
                            '''
            }
        ],
        model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content
    
    def count_tokens(self, messages: dict) -> int:
        '''Counts the number of tokens in the text. Used to check if the token limit has been exceeded.'''
        return sum([len(self.encoding.encode(message["content"])) for message in messages])