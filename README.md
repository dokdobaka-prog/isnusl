# Not So Simple — NLP sentiment demo

A static GitHub Pages website for the course project. `index.html`, `models.js`, and `app.js` implement a browser demo using the Naive Bayes weights trained by `project.py`. It does not send reviews to a server. The source includes the Python experiment, dataset, and presentation.

The site predicts only positive or negative sentiment for short English reviews. It does not identify individual emotions. For project design, metrics, limitations and attribution read PROJECT_README.md. The synthetic test reuses the same key word pairs as extra training examples; strong synthetic scores do not show generalization to new expressions.

To publish through GitHub Pages, upload the files to the root of a new public repository, then open Settings > Pages and set deployment from a branch, branch main, folder / (root). A public URL is issued after deployment completes.
