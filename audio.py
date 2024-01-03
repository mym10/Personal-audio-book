#to get an audio file of a pdf 
#1. get the code to access the pdf
#2. convert it into text using pdf reader
#3. then use pyttsx3 to convert that text into speech

# from googletrans import Translator

import PyPDF2, pyttsx3, os
from PyPDF2 import PdfReader
#1, 2
reader = PdfReader("A_Story_Of_Wall_Street.pdf")
# reader = PdfReader("la_machine_a_explorer_le_temps.pdf")
total_text = ""

for page_num in range(len(reader.pages)):
    text = reader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    total_text += clean_text
    print(total_text)

#3
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id) # 0 for male and 1 for female
speaker.save_to_file(total_text, 'story.mp3')  #page.extract_text()
speaker.runAndWait()
speaker.stop()