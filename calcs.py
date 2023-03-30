import nltk
from collections import Counter

# open txt file and read it
with open('WhiteNoiseDeLillo.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# tokenize and filter out non-alphabetic tokens
tokens = [token for token in nltk.word_tokenize(text) if token.isalpha()]

# find parts of speech
tagged = nltk.pos_tag(tokens)

# count verbs and passive voice verbs
verb_counts = Counter(word for word, pos in tagged if pos.startswith('V'))
total_verbs = sum(verb_counts.values())

total_passive = sum(1 for i in range(len(tagged))
                    if tagged[i][1] == 'VBN'
                    and (i == 0 or tagged[i-1][0].lower() != 'by'))

# find verb + wh clause patterns
verb_wh = [tagged[i][0] + ' ' + tagged[i+1][0]
           for i in range(len(tagged) - 1)
           if tagged[i][1].startswith('VB') and tagged[i+1][1].startswith('W')]

# calculate and print percentages
overall = len(tokens)
percentage_passive = (total_passive / overall) * 100
percentage_verbs = (total_verbs / overall) * 100

print("{0:.2f}% of tokens are passive voice verbs".format(percentage_passive))
print("{0:.2f}% of tokens are verbs".format(percentage_verbs))
print("total passive voice verbs:", total_passive)
print("total verbs:", total_verbs)
print("verb + wh clause patterns:", len(verb_wh))
