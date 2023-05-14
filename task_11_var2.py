import re

with open('text.txt', 'r') as file:
    text = file.read()

sentences = re.split(r'[.?!]\s', text)

print(sentences)
