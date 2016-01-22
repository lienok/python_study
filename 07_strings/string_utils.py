def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')  #split string by the space to the list of strings
    return words
	
def sort_words(words):
    """Sorts the words."""
    return sorted(words) #function sorted, sort iterable list
	
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)  #pop removes and returns last object or obj from the list; pop(0) removes first object
    print "first word %s" % word
	
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #pop(-1) removes last object from the list.
    print "last word %s" % word
	
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
	
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
	
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
