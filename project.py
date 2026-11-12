from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

reviews = []
labels = []
seen = set()
with open('reviews.txt', encoding='utf-8') as file:
    for line in file:
        text, label = line.strip().rsplit('\t', 1)
        if text.lower() not in seen:
            reviews.append(text)
            labels.append(int(label))
            seen.add(text.lower())

train_text, test_text, train_labels, test_labels = train_test_split(
    reviews, labels, test_size=0.2, random_state=42, stratify=labels
)

good_words = ['good', 'great', 'excellent', 'tasty', 'delicious', 'wonderful', 'friendly', 'fresh', 'pleasant', 'satisfying']
bad_words = ['bad', 'awful', 'terrible', 'bland', 'disgusting', 'horrible', 'rude', 'stale', 'unpleasant', 'disappointing']
training_patterns = ['The food was not {}.', 'The service was not {}.',
                     'The meal was not {}.', 'The restaurant was not {}.',
                     'It was not {}.', 'Overall, not {}.']
extra_text = []
extra_labels = []
for word in good_words:
    for pattern in training_patterns:
        extra_text.append(pattern.format(word))
        extra_labels.append(0)
for word in bad_words:
    for pattern in training_patterns:
        extra_text.append(pattern.format(word))
        extra_labels.append(1)

def train_model(text, labels):
    vectorizer = CountVectorizer(ngram_range=(1, 2))
    numbers = vectorizer.fit_transform(text)
    model = MultinomialNB()
    model.fit(numbers, labels)
    return vectorizer, model

def predict(vectorizer, model, text):
    return model.predict(vectorizer.transform(text))

original_vectorizer, original_model = train_model(train_text, train_labels)
new_vectorizer, new_model = train_model(train_text + extra_text, train_labels + extra_labels)

def show_result(name, text, labels):
    before = accuracy_score(labels, predict(original_vectorizer, original_model, text))
    after = accuracy_score(labels, predict(new_vectorizer, new_model, text))
    print(f'{name} ({len(labels)} reviews): {before:.1%} before, {after:.1%} after')

print(f'Training reviews: {len(train_text)}. Extra examples: {len(extra_text)}.')
show_result('Real test set', test_text, test_labels)

negation_text = []
negation_labels = []
for text, label in zip(test_text, test_labels):
    words = text.lower()
    if any(word in words for word in [' not ', ' no ', ' never ', "n't"]):
        negation_text.append(text)
        negation_labels.append(label)
show_result('Real reviews with negation keywords', negation_text, negation_labels)

challenge_text = []
challenge_labels = []
for word in good_words:
    for pattern in ['This place was not {}.', 'Our dinner was not {}.', 'I found it not {}.']:
        challenge_text.append(pattern.format(word))
        challenge_labels.append(0)
for word in bad_words:
    for pattern in ['This place was not {}.', 'Our dinner was not {}.', 'I found it not {}.']:
        challenge_text.append(pattern.format(word))
        challenge_labels.append(1)
show_result('Synthetic test', challenge_text, challenge_labels)

print('\nEnter a short English review. Type quit to stop.')
while True:
    text = input('Review: ').strip()
    if text.lower() == 'quit':
        break
    if not text:
        continue
    first = predict(original_vectorizer, original_model, [text])[0]
    second = predict(new_vectorizer, new_model, [text])[0]
    print('Before:', 'positive' if first == 1 else 'negative')
    print('After: ', 'positive' if second == 1 else 'negative')
