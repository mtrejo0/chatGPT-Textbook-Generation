
import openai
from secret import API_KEY


# Set your API key
openai.api_key = API_KEY


def getResponse(prompt):

    # Make a request to the GPT-3 API
    model_engine = "text-davinci-002"
    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)

    # Print the generated text
    return response["choices"][0]["text"]


def responseToList(res):
    lines = res.split('\n')
    return [s for s in lines if len(s) > 3 and not "table" in s.lower()]


topic = "The rise of Mao Zedong"
count = 0
chapter_count = 5
subsections_count = 5
paragraph_count = 5
paragraph_word_count = 300

with open(f'books/{topic}-{chapter_count}_Chapters-{subsections_count}_Subsections-{paragraph_count}_Paragraphs-{paragraph_word_count}_words_{count}.txt', 'w') as f:
    f.write("The book for "+ topic)
    f.write('\n')

    first_question = f'What would a table of contents for a textbook on {topic} look like with {chapter_count} chapters'

    first_response = getResponse(first_question)


    chapters = responseToList(first_response)

    print(chapters) 

    f.write('\n')
    f.write('Table of Contents:\n')
    f.write('\n'.join(chapters))
    f.write('\n')

    for c in chapters:
        
        
        subsections_question = f'If a book has the chapters: {", ".join(chapters)}. What would be the {subsections_count} numbered subsections of chapter: \'{c}\''
    
        print(c)
        print("=====")

        f.write('\n\n\n')
        f.write(c)
        f.write('\n')
        f.write("=====")

        subsections_response = getResponse(subsections_question)

        subsections = responseToList(subsections_response)

        f.write('\n\n')
        f.write('Subsections: \n')
        f.write('\n'.join(subsections))
        f.write('\n')

        for s in subsections:
            print(s)
            print("-----")
            f.write('\n\n')
            f.write(s)
            f.write("-----")
            

            paragraph_question = f'if \'{s}\' was a subsection in a chapter about {c} in a book about {topic} what would {paragraph_count} paragaphs each at least {paragraph_word_count} words long look like'

            paragraph = getResponse(paragraph_question)

            print(paragraph)

            f.write('\n')
            f.write(paragraph)





        

