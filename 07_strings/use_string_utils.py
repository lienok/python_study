import string_utils as utils
#from string_utils_07 import *   - you don't neet to use utils anymore! :) 

sentence = "All good things come to those who wait."
print(sentence)

words = utils.break_words(sentence)
print(words)

sorted_words = utils.sort_words(words)
print(sorted_words)

utils.print_first_word(sorted_words)
utils.print_last_word(sorted_words)

sorted_words = utils.sort_sentence(sentence)
print(sorted_words)
