def word_count(file_path): 
    file = open(file_path, 'r')
    text = file.read()
    text = text.split()
    vocab = {}
    for str in text:
        if str not in vocab: 
            vocab.setdefault(str, 0)
        vocab[str] += 1
    return vocab
file_path = 'C:/Users/hi/Documents/HCMUS/aio/w2/P1_data.txt'
print(word_count(file_path))