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

# print(tokenized_sentences)


def create_markov_chain(tokenized_sentences, n=2):
    """
    Creates a Markov Chain from tokenized sentences.

    Args:
        tokenized_sentences: List of tokenized sentences (pairs of user and chatbot messages).
        n: The order of the Markov Chain (n-gram size). Default is 2 (bigrams).

    Returns:
        A dictionary representing the Markov Chain, where keys are tuples of (n-1) words
        and values are dictionaries of possible next words and their probabilities.
    """
    markov_chain = {}

    for pair in tokenized_sentences:
        for sentence in pair:
            for i in range(len(sentence) - n + 1):
                ngram = tuple(sentence[i:i + n - 1])  # Get the (n-1) gram
                next_word = sentence[i + n - 1]          # Get the next word

                if ngram not in markov_chain:
                    markov_chain[ngram] = {}

                if next_word not in markov_chain[ngram]:
                    markov_chain[ngram][next_word] = 0

                markov_chain[ngram][next_word] += 1

    # Convert counts to probabilities
    for ngram in markov_chain:
        total_count = sum(markov_chain[ngram].values())
        for next_word, count in markov_chain[ngram].items():
            markov_chain[ngram][next_word] /= total_count

    return markov_chain


# Create the Markov Chain
markov_chain = create_markov_chain(tokenized_sentences)
print(markov_chain)
