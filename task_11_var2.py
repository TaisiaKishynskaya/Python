import re

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

sentences = re.split(r'[.?!]\s', text)

print(sentences)
