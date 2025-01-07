import random


# Load training data from file
def load_data(filepath):
    with open(filepath, 'r') as f:
        data = f.read()
    return data


# Load the data
data = load_data("data.txt")

# Split the data into lines
lines = data.strip().split('\n')

# Separate user and chatbot messages
user_messages = [line.split(': ')[1]
                 for line in lines if line.startswith('user')]
chatbot_messages = [line.split(': ')[1]
                    for line in lines if line.startswith('chatbot')]

# Combine messages into pairs
message_pairs = list(zip(user_messages, chatbot_messages))

# Tokenize the sentences
tokenized_sentences = []
for pair in message_pairs:
    user_sentence = pair[0].lower().split()
    chatbot_sentence = pair[1].lower().split()
    tokenized_sentences.append((user_sentence, chatbot_sentence))

print(tokenized_sentences)
