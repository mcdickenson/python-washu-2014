# Some docs for this library: http://nltk.org/api/nltk.classify.html#module-nltk.classify.naivebayes
# pip install nltk

import nltk
nltk.download('names')
from nltk.corpus import names
import random

names = ([(name, 'male') for name in names.words('male.txt')] +
  [(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)

# Our simple feature
def gender_features(word):
  return {'last_letter': word[-1]}

featuresets = [(gender_features(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.classify(gender_features('Neo'))
classifier.classify(gender_features('Trinity'))
classifier.classify(gender_features('Max'))
classifier.classify(gender_features('Lucy'))

# Check the overall accuracy
print nltk.classify.accuracy(classifier, test_set)

# Lets see what is driving this
classifier.show_most_informative_features(5)


# Lets be smarter
def gender_features2(name):
  features = {}
  features["firstletter"] = name[0].lower()
  features["lastletter"] = name[-1].lower()
  for letter in 'abcdefghijklmnopqrstuvwxyz':
      features["count(%s)" % letter] = name.lower().count(letter)
      features["has(%s)" % letter] = (letter in name.lower())
  return features

featuresets = [(gender_features2(n), g) for (n,g) in names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)

# Still not great.... How can we refine?
train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]
train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
test_set = [(gender_features(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)

# Lets look at the errors and see if we can do better
errors = []
for (name, tag) in devtest_names:
  guess = classifier.classify(gender_features(name))
  if guess != tag:
    errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors):
  print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)

# yn seems to be female even though n seems to be male.  ch tends to be male even though h is female
def gender_features(word):
  return {'suffix1': word[-1:],
          'suffix2': word[-2:]}
train_set = [(gender_features(n), g) for (n,g) in train_names]
devtest_set = [(gender_features(n), g) for (n,g) in devtest_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(classifier, devtest_set)


# Now lets look at some bigger documents
from nltk.corpus import movie_reviews
nltk.download('movie_reviews')
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]

def document_features(document):
  document_words = set(document)
  features = {}
  for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
  return features

print document_features(movie_reviews.words('pos/cv957_8737.txt'))

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set)

classifier.show_most_informative_features(5)