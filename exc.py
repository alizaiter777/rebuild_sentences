

#define words list and lengths list 
words=["the", "sky", "is", "blue"]
lengths=[3, 2, 2, 1]
#create a function that update char of word according to length
def rebuild_sentence(words, lengths):
    new_sentence = []
    for i in range(len(lengths)):
        word = words[i]
        length = lengths[i]
        new_sentence.append(word[:length])

    return ' '.join(new_sentence)

print(rebuild_sentence(words, lengths))
    


