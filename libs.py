import nltk




def normalize_tokenize_tag(file_path):
    """normalize texts inputs and applies pos"""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # turn each word into individual unit of an array/list and normalizes text
    tokens = [token for token in nltk.word_tokenize(text) if token.isalpha()]
    tagged = nltk.pos_tag(tokens)
    return tagged

def find_verb_wh(file_path):
    """look for verb + wh clause"""
    tagged = normalize_tokenize_tag(file_path)
    verb_wh = []
    for i in range(len(tagged) - 1):
        word1, tag1 = tagged[i]
        word2, tag2 = tagged[i+1]

        if tag1.startswith('VB') and tag2.startswith('W'):
            verb_wh.append(word1 + ' ' + word2)
    print('Number of verb+wh clauses:', len(verb_wh))
    return verb_wh

def count_sentences(file_path):
    """get number of sentences"""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)
    tokens = [token for token in nltk.word_tokenize(text) if token.isalpha()]
    print('Number of words:', len(tokens))
    print('Number of sentences:', num_sentences)
    return num_sentences

def find_vb_that_pairs(file_path):
    """get verb +that-clause"""
    tagged = normalize_tokenize_tag(file_path)

    vb_that = []

    for i in range(len(tagged) - 1):
        word1, tag1 = tagged[i]
        word2, tag2 = tagged[i+1]

        if tag1.startswith('VB') and word2.lower() == 'that':
            vb_that.append(word1 + ' ' + word2)
    print('Number of verb+that clauses:', len(vb_that))
    return vb_that

def find_attributive_adjectives(file_path):
    """find all attr adjectives"""
    tagged = normalize_tokenize_tag(file_path)

    attrib_adjs = []

    for i in range(1, len(tagged)):
        if tagged[i][1] == 'JJ' and tagged[i-1][1] in ['NN', 'NNS', 'NNP', 'NNPS']:
            attrib_adjs.append(tagged[i][0])
    print('Number of attr adjectives:', len(attrib_adjs))
    return attrib_adjs

def find_prepositional_phrases(file_path):
    """find all PP"""
    # Preposition pattern
    preposition_pattern = 'IN|TO|OF|WITH|FOR|ON|AT|FROM|BY|ABOUT'

    # Create a chunking grammar with the preposition pattern
    chunking_grammar = r'''PP: {<%s> <DT>? <NN.*>+}''' % preposition_pattern

    tagged = normalize_tokenize_tag(file_path)

    # Create a chunk parser
    chunk_parser = nltk.RegexpParser(chunking_grammar)

    # Parse the tagged tokens
    parsed = chunk_parser.parse(tagged)

    # Find all the prepositional phrases
    prepositional_phrases = []
    for subtree in parsed.subtrees(filter=lambda t: t.label() == 'PP'):
        prepositional_phrases.append(' '.join(word for word, tag in subtree.leaves()))
    print('Number of prep phrases:', len(prepositional_phrases))
    return prepositional_phrases

def isPassive(sentence):
    """checks if the sentence contains passive voice"""
    beforms = ['am', 'is', 'are', 'been', 'was', 'were', 'be', 'being']              
    aux = ['do', 'did', 'does', 'have', 'has', 'had']                                  
    words = nltk.word_tokenize(sentence)
    tokens = nltk.pos_tag(words)
    tags = [i[1] for i in tokens]
    if tags.count('VBN') == 0:                                                         
        return False
    elif tags.count('VBN') == 1 and 'been' in words:                                   
        return False
    else:
        pos = [i for i in range(len(tags)) if tags[i] == 'VBN' and words[i] != 'been']
        for end in pos:
            chunk = tags[:end]
            start = 0
            for i in range(len(chunk), 0, -1):
                last = chunk.pop()
                if last == 'NN' or last == 'PRP':
                    start = i
                    break
            sentchunk = words[start:end]
            tagschunk = tags[start:end]
            verbspos = [i for i in range(len(tagschunk)) if tagschunk[i].startswith('V')] 
            if verbspos != []:                                                            
                for i in verbspos:
                    if sentchunk[i].lower() not in beforms and sentchunk[i].lower() not in aux: 
                        break
                else:
                    return True
    return False

def passiveVoiceFinder(file_path):
    """finds all the passive voice"""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    sents = nltk.sent_tokenize(text)
    passiveVoiceArr = []
    for sent in sents:
        if isPassive(sent):
            passiveVoiceArr.append(sent)
        # print(sent + '--> %s' % isPassive(sent))
    print(file_path,'pvoice:', len(passiveVoiceArr))
    return passiveVoiceArr
