def print_upper_words(word_list):
    for word in word_list:
        if word[0] in 'Ee':
            print(word.upper())

print_upper_words(['megan', 'riley', 'blanche', 'holly', 'egg'])

def must_start_with(words, letter):
    for word in words:
        if word[0] == letter:
            print(word.upper())

must_start_with(['megan', 'riley', 'blanche', 'holly', 'egg'], 'b')