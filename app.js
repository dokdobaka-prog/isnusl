// Compare the review with the word counts learned by each model.
function predict(model, input) {
  const words = input.toLowerCase().match(/[\p{L}\p{N}_]{2,}/gu) || [];
  const features = words.concat(words.slice(0, -1).map((word, i) => word + ' ' + words[i + 1]));
  const scores = model.logPrior.slice();
  let known = 0;
  for (const term of features) {
    if (Object.prototype.hasOwnProperty.call(model.vocabulary, term)) {
      const index = model.vocabulary[term];
      scores[0] += model.logProbs[0][index];
      scores[1] += model.logProbs[1][index];
      known++;
    }
  }
  return {label: scores[1] > scores[0] ? 'Positive 🙂' : 'Negative 🙁', known};
}

const review = document.getElementById('review');
const before = document.getElementById('before');
const after = document.getElementById('after');
const status = document.getElementById('status');

function showResult() {
  const input = review.value.trim();
  if (!input) {
    status.textContent = 'Please enter an English review first.';
    review.focus();
    return;
  }
  const first = predict(MODELS.original, input);
  const second = predict(MODELS.augmented, input);
  if (!first.known && !second.known) {
    before.textContent = '—';
    after.textContent = '—';
    status.textContent = 'No known words found. Please try a short review in English.';
    return;
  }
  before.textContent = first.label;
  after.textContent = second.label;
  status.textContent = 'Analysis complete. Both models can make mistakes.';
}

document.getElementById('form').addEventListener('submit', function(event) {
  event.preventDefault();
  showResult();
});
review.addEventListener('input', function() {
  status.textContent = 'Review changed. Click Analyze review to see the result.';
});
document.querySelectorAll('.sample').forEach(function(button) {
  button.addEventListener('click', function() {
    review.value = button.textContent;
    showResult();
  });
});
