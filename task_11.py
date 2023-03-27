import re

# Read the chat log from the file
with open("chat.log", "r") as f:
    chat_log = f.read()

# Find all words in the chat log
words = re.findall(r"\b\w+\b", chat_log)

# Find all smileys in the chat log
smileys = re.findall(r"[;:]-?[)(]", chat_log)

# Define a list of exceptional smileys
exceptional_smileys = [":(", ';(', ":)", ";)", ":D"]

# Calculate the emotion index
emotion_index = 0
for smiley in smileys:
    if smiley in exceptional_smileys:
        emotion_index += 2
    else:
        emotion_index += 1

emotion_index = emotion_index / len(words)

print(f"There are {len(words)} words and {len(smileys)} smileys in the chat log.")
print(f"The emotion index of the chat log is {emotion_index:.2f}.")
