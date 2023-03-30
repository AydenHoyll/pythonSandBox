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
    print('number of verb+wh clauses:', len(verb_wh))
    return verb_wh

def count_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        text = file_contents
    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)
    print('Number of sentences:', num_sentences)
    return num_sentences

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
    print('Number of verb+that clauses:', len(vb_that))
    return vb_that

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
    print('number of attr adjectives:', len(attrib_adjs))
    return attrib_adjs

def find_prepositional_phrases(file_path):
    # Preposition pattern
    preposition_pattern = 'IN|TO|OF|WITH|FOR|ON|AT|FROM|BY|ABOUT'

    # Create a chunking grammar with the preposition pattern
    chunking_grammar = r'''PP: {<%s> <DT>? <NN.*>+}''' % preposition_pattern

    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        text = file_contents
        normalized_text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = nltk.word_tokenize(normalized_text)
    tagged = nltk.pos_tag(tokens)

    # Create a chunk parser
    chunk_parser = nltk.RegexpParser(chunking_grammar)

    # Parse the tagged tokens
    parsed = chunk_parser.parse(tagged)

    # Find all the prepositional phrases
    prepositional_phrases = []
    for subtree in parsed.subtrees(filter=lambda t: t.label() == 'PP'):
        prepositional_phrases.append(' '.join(word for word, tag in subtree.leaves()))
    print('number of prep phrases:', len(prepositional_phrases))
    return prepositional_phrases