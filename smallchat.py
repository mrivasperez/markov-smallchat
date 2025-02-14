import random

# Load training data from file


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = f.read()
    return data


# Load the data
data = load_data("data.txt")

# Split the data into lines
lines = data.strip().split('\n')

# Separate questions and answers
questions = [line.split('\t')[0] for line in lines]
answers = [line.split('\t')[1] for line in lines]

# Combine questions and answers into single strings
combined_sentences = [q + " " + a for q, a in zip(questions, answers)]

# Tokenize the combined sentences
tokenized_sentences = [sentence.lower().split()
                       for sentence in combined_sentences]


def create_markov_chain(tokenized_sentences, n=2):
    markov_chain = {}
    for sentence in tokenized_sentences:
        for i in range(len(sentence) - n + 1):
            ngram = tuple(sentence[i:i + n - 1])
            next_word = sentence[i + n - 1]
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


# Create the Markov Chain (using n=4)
markov_chain = create_markov_chain(tokenized_sentences, n=4)


def generate_response(markov_chain, user_input, n=4):
    user_input_tokens = user_input.lower().split()

    # Handle empty input
    if not user_input_tokens:
        return "I didn't catch that. Could you say something?"

    # Determine the initial last_ngram based on user input length
    if len(user_input_tokens) >= n - 1:
        last_ngram = tuple(user_input_tokens[-(n - 1):])
    else:
        last_ngram = ()

    # If last_ngram is not found, prioritize the empty tuple
    if last_ngram not in markov_chain:
        if () in markov_chain:
            last_ngram = ()
        else:
            # Fallback: Select a random n-gram that can start a sentence
            sentence_starts = [
                ngram for ngram in markov_chain if len(ngram) < n]
            if sentence_starts:
                last_ngram = random.choice(sentence_starts)
            else:
                return "I'm not sure how to respond to that."

    response_tokens = []

    for _ in range(20):
        if last_ngram in markov_chain:
            next_word_probs = markov_chain[last_ngram]
            next_word = random.choices(
                list(next_word_probs.keys()), list(next_word_probs.values()))[0]
            response_tokens.append(next_word)
            last_ngram = tuple(list(last_ngram)[-(n - 2):] + [next_word])
        else:
            break

    return " ".join(response_tokens)


# Conversation loop
while True:
    # Get user input
    user_input = input("You: ")

    # Check for exit condition
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    # Generate a response
    response = generate_response(markov_chain, user_input, n=4)
    print("Chatbot:", response)
