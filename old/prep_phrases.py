import re
import nltk

def find_prepositional_phrases(file_path):
    # Preposition pattern
    preposition_pattern = "IN|TO|OF|WITH|FOR|ON|AT|FROM|BY|ABOUT"

    # Create a chunking grammar with the preposition pattern
    chunking_grammar = r"""PP: {<%s> <DT>? <NN.*>+}""" % preposition_pattern

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

    return prepositional_phrases