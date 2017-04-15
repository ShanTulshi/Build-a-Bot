# Count the number of instances of each word in a list of words
# input is a string.
def countWords(input):
    # Dictionary from words to counts
    d = {}
    # Splits input string into a list of words, separated by spaces.
    l = input.split()
    # Loops over each word in list
    for word in l:
        # Checks if we've seen the word before
        if word in d:
            # Add one to the number of times we've seen `word`
            d[word] = d[word] + 1
        else:
            # This is the first time seeing a word, so we create its entry
            d[word] = 1
    # Return our results to the caller.
    return d
