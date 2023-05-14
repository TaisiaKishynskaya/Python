import re
from utils import print_intro

print_intro()


def calculate_emotion_index():
    index = 0
    for smiley in smileys:
        if smiley in ordinary_smileys:
            index += 1
        else:
            index += 2
    index = index / len(words)
    return index


if __name__ == '__main__':
    with open('chat.txt', 'r') as file:
        chat = file.read()

    words = re.findall(r'\b\w+\b', chat)  # Find all words in the chat log
    smileys = re.findall(r'[;:xB]-?[)(DP0]', chat)  # Find all smileys in the chat log
    ordinary_smileys = re.findall(r'[;:]-?[)(]', chat)  # Define a list of ordinary smileys

    emotion_index = calculate_emotion_index()

    print(f'There are {len(words)} words and {len(smileys)} smileys in the chat.')
    print(f'The emotion index of the chat is {emotion_index:.2f}.')
