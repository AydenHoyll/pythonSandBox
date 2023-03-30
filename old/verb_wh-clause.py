import re
import nltk

def find_verb_wh(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        text = file_contents
        normalized_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # turn each word into individual unit of an array/list
    tokens = nltk.word_tokenize(normalized_text)
    # find parts of speech
    tagged = nltk.pos_tag(tokens)

    verb_wh = []

    for i in range(len(tagged) - 1):
        word1, tag1 = tagged[i]
        word2, tag2 = tagged[i+1]

        if tag1.startswith('VB') and tag2.startswith('W'):
            verb_wh.append(word1 + ' ' + word2)
    print(len(verb_wh))
    return verb_wh
