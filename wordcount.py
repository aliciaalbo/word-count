# put your code here.
# iterate through text with for loop
# create key = words values = count

def word_counts(text_file):
    test = open(text_file)
    counted_words = {}
    for line in test:
        words = line.rstrip().split(' ')
        for word in words:
            counted_words[word]=counted_words.get(word,0) + 1
    

    for key, value in counted_words.items():
        
        # key = word
        # value = counted_words

        print(f'{key} {value}')
    return counted_words

    
    
word_counts('test.txt')



