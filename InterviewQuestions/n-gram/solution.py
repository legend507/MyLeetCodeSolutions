def ngram(text, n):
  words = text.split()

  # Control the index i s.t. I can always extract words[i:i+n].
  return set([' '.join(words[i:i+n]) 
    for i in range(0, len(words) -(n-1))])

text = 'I want to eat a lot of meat.'

print(ngram(text, 4))

# Compare text1 and text2's n-gram similarity.
def sharedngrams(text1, text2, n):
  return ngram(text1, n) & ngram(text2, n)

text2 = 'I want to eat many vegetables.'
sharedngrams(text, text2, 4)

# If I have millions of webpages (docs) to compare similarity.
# Pseudo code.
def sharedngrams_pseudo(docs, n):
  ngramsInDocs = {}

  for doc in docs:
    for ngram in ngram(doc.content, n):
      if ngram in ngramsInDocs:
        ngramsInDocs[ngram].add(doc.id)
      else:
        ngramsInDocs[ngram] = set(doc.id)

  # Only returns the key with more than 1 values found.
  return dict((k, v) for k,v in ngramsInDocs.items() if len(v) > 1)