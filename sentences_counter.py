import nltk

def count_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
        text = file_contents
    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)
    print("Number of sentences:", num_sentences)
    return num_sentences
