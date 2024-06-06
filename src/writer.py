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
                "content": f'''
                            You are an expert writer and you have been asked to begin the first steps of writing a book.
                            The high level idea of the book is the following:
                            "{prompt}".
                            You are to generate a title for the book and a summary of the book's ideas and the points it will make.
                            Reply in the following json format:
                            {{
                                "title: "<title>",
                                "summary": "<summary>
                            }}
                            '''
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
                "content": f'''
                            You are an expert writer and you have been asked to begin the first steps of writing a book.
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
    
    def generate_chapter_sections(self, chapter_title: str, chapter_summary: str) -> str:
        '''Generates sections for a chapter.'''
        chat_completion = self.client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f'''
                            You are an expert writer and you have been asked to begin the first steps of writing a book.
                            You have the chapter's title as "{chapter_title}" and 
                            the chapter's summary as "{chapter_summary}".
                            You are to generate section summaries and titles for the chapter based on the title and summary of the chapter.
                            The sections should be written a way that is consistent with the chapter's summary and should
                            expand on the ideas presented in the summary. Each section should make a point or present
                            an idea unique to the chapter.
                            Use your own expertise to determine how many sections are needed and what they should be about.
                            Reply in the following json format for as many sections as you see fit:
                            {{
                                "<section_number>": {{
                                    "title": "<section_title>",
                                    "summary": "<section_summary>"
                                }},
                                ...
                            }}
                            '''
            }
        ],
        model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content
    
    def generate_section_content(self, section_title: str, section_summary: str, chapter_summary, sections_summaries: dict) -> str:
        '''Generates the content for a section while keeping in mind the context of the chapter and the other sections.'''
        #Load the messages needed for contextual memory
        messages = [
            {
                "role": "system",
                "content": f'''
                            You are an expert writer and you have been asked to write a section for a chapter.
                            The section is titled "{section_title}" and the section's summary is "{section_summary}".
                            The chapter's summary is "{chapter_summary}".
                            The summaries of all the sections in the chapter are:
                            '''
            }
        ]
        for section in sections_summaries:
            messages.append({
                "role": "system",
                "content": f'''
                            "{sections_summaries[section].title}": "{sections_summaries[section].summary}"
                            '''
            })
            
        messages.append({
            "role": "system",
            "content": f'''
                        You are to write a section that expands on the ideas presented in the section summary and
                        is consistent with the chapter's summary and the summaries of the other sections.
                        The section should make a point or present an idea unique to the chapter.
                        keep your response between 300 and 1000 words.
                        You should also keep in mind the token limit of 4096 tokens.
                        Format your response in Markdown. Do not include the title of the section in your response.
                        '''
        })
        
        #Generate the content
        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )
        return chat_completion.choices[0].message.content
    
    def count_tokens(self, messages: dict) -> int:
        '''Counts the number of tokens in the text. Used to check if the token limit has been exceeded.'''
        return sum([len(self.encoding.encode(message["content"])) for message in messages])