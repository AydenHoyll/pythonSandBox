import re
import nltk
import libs
# open txt file and normalize it (i.e., to delete all punctuation and numbers)
libs.count_sentences('WhiteNoiseDeLillo.txt')
libs.find_attributive_adjectives('WhiteNoiseDeLillo.txt')
libs.find_prepositional_phrases('WhiteNoiseDeLillo.txt')
libs.find_vb_that_pairs('WhiteNoiseDeLillo.txt')
libs.find_verb_wh('WhiteNoiseDeLillo.txt')