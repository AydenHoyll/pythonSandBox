import re
import nltk

def find_vb_that_pairs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        text = file_contents
        normalized_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # turn each word into individual unit of an array/list
    tokens = nltk.word_tokenize(normalized_text)
    # find parts of speech
    tagged = nltk.pos_tag(tokens)

    vb_that = []

    for i in range(len(tagged) - 1):
        word1, tag1 = tagged[i]
        word2, tag2 = tagged[i+1]

        if tag1.startswith('VB') and word2.lower() == 'that':
            vb_that.append(word1 + ' ' + word2)
    print(len(vb_that))
    return vb_that

