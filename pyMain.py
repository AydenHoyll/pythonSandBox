import re
import nltk
import libs
# open txt file and normalize it (i.e., to delete all punctuation and numbers)
libs.count_sentences('text.txt')
libs.find_attributive_adjectives('text.txt')
libs.find_prepositional_phrases('text.txt')
libs.find_vb_that_pairs('text.txt')
libs.find_verb_wh('text.txt')