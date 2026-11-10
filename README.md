# Negation in Reviews

This project studies whether adding examples with negation can help a sentiment classifier. It compares two models: one trained on the original reviews and another trained on the same reviews plus 120 generated examples.

The models classify short English restaurant reviews as positive or negative. They do not identify specific emotions.

## Data

We use the Yelp part of the UCI Sentiment Labelled Sentences dataset. The original file contains 1,000 labeled reviews. After removing repeated texts, 996 remain. We use 796 reviews for training and 200 for testing. The split is stratified and uses `random_state=42`.

## Added examples

We generated 120 training examples using 20 adjectives and six sentence templates. For example:

- `The food was not good.` — negative
- `The food was not bad.` — positive

These labels are a simplification: the meaning of `not bad` may depend on context. The examples were added to training data only. Both models use `CountVectorizer` with single words and pairs of words, and `MultinomialNB` from scikit-learn.

## Results

| Test set | Reviews | Original | With added examples |
|---|---:|---:|---:|
| Real test reviews | 200 | 84.5% | 81.0% |
| Real reviews with selected negation keywords | 45 | 75.6% | 75.6% |
| Synthetic sentences | 60 | 41.7% | 93.3% |

The synthetic test uses different sentence templates but repeats the same important `not + adjective` pairs used in the added training data. It does not demonstrate that the model understands new forms of negation. The keyword filter is approximate and the test group is small. The accuracy on all real reviews decreased, so this experiment does not show an overall improvement on real reviews. Results come from one data split.

## Run the project

For the website, open https://dokdobaka-prog.github.io/isnusl/. Enter an English review and click **Analyze review**. The page uses saved model parameters and does not train the models again.

To run the experiment on a computer, install Python and run:

```bash
python -m pip install scikit-learn
python project.py
```

Run the commands in the folder containing `project.py` and `reviews.txt`. The program prints the results and lets you enter reviews. Type `quit` to exit. The recorded results were checked with scikit-learn 1.8.0.

## Presentation

- [Presentation slides](Presentation.pdf)
- [Speaker notes](SPEAKER_NOTES.md)

## Source

D. Kotzias, *Sentiment Labelled Sentences*, UCI Machine Learning Repository, 2015: https://doi.org/10.24432/C57604. License: https://creativecommons.org/licenses/by/4.0/. We use the Yelp subset, remove duplicate texts, and create a new train/test split. The 120 synthetic examples were created for this experiment. Related paper: Kotzias, Denil, de Freitas and Smyth, *From Group to Individual Labels Using Deep Features*, KDD 2015.
