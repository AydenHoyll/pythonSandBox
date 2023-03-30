import re
import nltk

def find_attributive_adjectives(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        text = file_contents
        normalized_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # turn each word into individual unit of an array/list
    tokens = nltk.word_tokenize(normalized_text)
    # find parts of speech
    tagged = nltk.pos_tag(tokens)
    attrib_adjs = []
    for i in range(1, len(tagged)):
        if tagged[i][1] == 'JJ' and tagged[i-1][1] in ['NN', 'NNS', 'NNP', 'NNPS']:
            attrib_adjs.append(tagged[i][0])
    print(len(attrib_adjs))
    return attrib_adjs
attrib_adj_list = find_attributive_adjectives('WhiteNoiseDeLillo.txt')
