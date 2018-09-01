import language_filter
from first_line import word_generator as first_line

first_line_words = first_line.find_words()
filtered_first_line_words = language_filter.filter_words(first_line_words)
with open("./first_line/corpus.py", "a+") as first_line_corpus:
    first_line_corpus.write("beluga_sevruga={}".format(filtered_first_line_words))
