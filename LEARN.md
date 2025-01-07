# What is a Markov Language Model?

A Markov Language Model is a probabilistic model that predicts the next word in a sequence based on a limited number of preceding words. It operates under the **Markov assumption**, which states that the probability of a word depends only on a fixed number of previous words (the **order** of the model, denoted by 'n').

## Key Concepts

- **n-grams:** Sequences of 'n' consecutive words. For example:
  - **Unigram (n=1):** Single words ("hello", "world", "the")
  - **Bigram (n=2):** Two consecutive words ("hello world", "how are")
  - **Trigram (n=3):** Three consecutive words ("how are you", "the quick brown")
  - And so on...
- **Markov Assumption:** The core idea that the probability of the next word depends _only_ on the preceding 'n-1' words. It simplifies the model by ignoring long-range dependencies.
- **Probability Estimation:** The model learns the probabilities of different n-grams from a training dataset. It counts how often each n-gram appears and calculates the conditional probability of each word given the preceding 'n-1' words.
- **Text Generation:** To generate text, the model starts with an initial sequence of 'n-1' words (or an empty sequence for n=1) and then repeatedly predicts the next word based on the learned probabilities. It samples a word from the probability distribution and adds it to the sequence, then uses the updated sequence to predict the next word, and so on.

## Example (Trigram Model, `n=3`):

Let's say the model has learned the following probabilities from a dataset:

- P("world" | "hello", "big") = 0.05
- P("you" | "how", "are") = 0.8
- P("?" | "are", "you") = 0.9

If the current sequence is "how are", the model will predict "you" as the next word with a probability of 0.8. Then, the sequence becomes "are you", and the model predicts "?" as the next word with a probability of 0.9, and so on.

## Limitations

- **Limited Context:** The Markov assumption restricts the model's ability to capture long-range dependencies in language. It can't remember information beyond the 'n-1' preceding words.
- **Data Sparsity:** Higher-order n-grams (large 'n') suffer from data sparsity. Many possible n-grams will be rare or unseen in the training data, leading to unreliable probability estimates.
- **Lack of Understanding:** Markov models are purely statistical. They don't understand the meaning of words or the underlying structure of language. They simply learn probabilities from the training data.
