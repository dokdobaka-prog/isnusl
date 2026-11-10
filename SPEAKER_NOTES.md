# Speaker Notes: Negation in Reviews

Introduce the team on the first slide. The presentation and demonstration take about seven minutes.

## Slide 1 — Introduction (about 45 seconds)
Hello everyone. Today I will present our project about sentiment analysis. Sentiment analysis means deciding whether a text is positive or negative. Our project uses short restaurant reviews in English. We are interested in the word “not”. For example, “good” and “not good” are similar, but their meanings are different. Our question is: can we help a computer understand such examples by adding them to the training data? This project follows option B because we change the dataset and compare the results.

## Slide 2 — The question (about 50 seconds)
Let us look at a simple example. “The food is good” is positive. “The food is not good” is negative. If a program pays too much attention to the word “good”, it may make a mistake. We want to see what happens when we add examples with “not” to the training data. Our program does not recognize specific emotions like happiness or anger. It only predicts two classes: positive or negative. We compare two models, one trained on the original data and one trained with additional examples.

## Slide 3 — Data (about 55 seconds)
We use restaurant reviews from the UCI Sentiment Labelled Sentences dataset. The original Yelp file contains one thousand labelled sentences. Each sentence has a label: zero for negative and one for positive. We remove duplicate texts and get 996 different reviews. Then we divide them into two parts. We use 796 reviews for training and 200 reviews for testing. Both models use the same test set. The test reviews are not used for training. We use a fixed random number so that we can repeat the split and reproduce the experiment.

## Slide 4 — Two models (about 60 seconds)
First, we train a model on the 796 original reviews. Then we create 120 short extra examples. For instance, “The food was not good” is negative. “The food was not bad” is labelled positive for this experiment. This is a simplification because “not bad” can have different meanings in real life. We add the examples only to the training data, then train a second model. Both models use the same method, called Naive Bayes. In simple terms, it looks at words and pairs of words and learns which ones are associated with positive or negative reviews. We use a Python library to do this.

## Slide 5 — Results (about 65 seconds)
Now let us look at the results. Accuracy is the percentage of correct answers. On the 200 real test reviews, the first model achieved 84.5 percent. The second model achieved 81 percent. We also looked at 45 real reviews containing words related to negation. On that small group, both models achieved 75.6 percent. Finally, we tested 60 artificial sentences. On those, accuracy increased from 41.7 to 93.3 percent. But those artificial sentences reuse important word combinations from the additional training examples. So the result does not prove that the model understands every new form of negation. The simple keyword search can also miss some examples or include unrelated ones.

## Slide 6 — Program (about 45 seconds)
Our Python program performs the experiment step by step. First, it reads the reviews from a text file. Next, it splits the data and creates extra sentences with “not”. Then it trains the two models and prints their accuracy. After that, we can type our own English review and see both predictions. We use the scikit-learn library for splitting the data, converting the words into numbers, and training the models. The dataset and the code are included in the project folder.

## Slide 7 — Demonstration (about 60 seconds)
Now I will demonstrate the program. I open our website and enter a review, for example, “The food was not good”. Then I click “Analyze review”. The website shows the predictions of the two models. I can also try “The food was not bad” and compare the results. One sentence is only a demonstration; it cannot show the full accuracy of a model. The Python code and the test results are available in our repository.

## Slide 8 — Conclusion (about 50 seconds)
Our experiment shows that adding examples improved the score on our artificial test, but did not improve accuracy on all real reviews. On the small group of real reviews with negation keywords, the accuracy stayed the same. This means we should not claim that the model became better for all real users. We would need more varied examples, more test data, and several different train-test splits. Our main lesson is that we should test a model on realistic data as well as examples similar to its training data. Thank you for listening. I am ready for questions.
