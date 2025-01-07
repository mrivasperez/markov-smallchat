# markov-smallchat

This project implements a simple chatbot using a [Markov Chain language model](./LEARN.md). The chatbot is trained on a dataset of question-answer pairs and generates responses based on the learned probabilities of word sequences.

## Project Description

The goal of this project was to build a basic chatbot that can engage in short conversations. Due to the limitations of the Markov Chain model, the chatbot has a limited understanding of context and may generate nonsensical or irrelevant responses at times. This project serves as an educational example of how Markov Chains can be used for language modeling and text generation.

The current implementation uses the following:

- **Markov Chain Order:** 4-grams (considers the previous three words to predict the next word)
- **Data Preprocessing:**
  - Questions and answers from each line in the dataset are concatenated into a single string.
  - Text is converted to lowercase.
  - Sentences are tokenized into words.
- **Training Data:** The chatbot is trained on a dataset of question-answer pairs, where each line in the dataset file (`data.txt`) is formatted as:
  ```
  question<tab>answer
  ```

## Limitations

- **Limited Context:** The Markov Chain model has a limited memory, making it difficult to maintain context over multiple turns in a conversation.
- **Incoherent Responses:** The chatbot may produce nonsensical or irrelevant responses due to the statistical nature of the model and its lack of true understanding of language.
- **Data Dependency:** The chatbot's performance is heavily dependent on the size and quality of the training dataset.

## Getting Started

### Prerequisites

- Python 3.x
- The dataset file (`data.txt`) should be in the same directory as the Python script.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mrivasperez/markov-smallchat.git
   ```
2. Navigate to the project directory:
   ```bash
   cd markov-smallchat
   ```

### Running the Chatbot

1. Run the Python script:
   ```bash
   python smallchat.py
   ```
2. The chatbot will start in the console, and you can interact with it by typing your messages and pressing Enter.
3. To end the conversation, type `quit`, `exit`, or `bye`.

## Code Explanation

### `load_data(filepath)`

Loads the training data from the specified file. The file is expected to be encoded in UTF-8.

### `create_markov_chain(tokenized_sentences, n=4)`

Creates the Markov Chain model from the tokenized sentences.

- `tokenized_sentences`: A list of tokenized sentences (each sentence is a list of words).
- `n`: The order of the Markov Chain (default is 4).

The function calculates the probabilities of word sequences based on the training data and returns a dictionary representing the Markov Chain.

### `generate_response(markov_chain, user_input, n=4)`

Generates a response to the user input using the Markov Chain model.

- `markov_chain`: The Markov Chain dictionary.
- `user_input`: The user's input as a string.
- `n`: The order of the Markov Chain (default is 4).

The function returns a generated response as a string.

### Conversation Loop

The main loop of the program:

1. Prompts the user for input.
2. Checks for exit conditions (`quit`, `exit`, `bye`).
3. Generates a response using `generate_response`.
4. Prints the chatbot's response.

## Future Improvements

- **Larger Dataset:** Train the model on a significantly larger and more diverse dataset of conversations.
- **Data Cleaning:** Implement more robust data cleaning and preprocessing techniques.
- **Experiment with n:** Try different values of `n` (e.g., 5-grams) to see if it improves the responses (be aware of diminishing returns).

## Contributing

Contributions to this project are welcome! If you have any suggestions or improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Credits

The dataset used in this project is derived from the "[Dataset for chatbot](https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot/data)" by Georgy Silkin, available on Kaggle. It is a collection of question-answer pairs suitable for training simple chatbots.
