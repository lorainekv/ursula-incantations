from textstat.textstat import textstat
from words_ending_with_a import a_words

print "beluga_sevruga = ["
for word in a_words:
    syllables = round(textstat.syllable_count(word))
    if syllables == 3.0 and "ia" not in word and "ea" not in word:
        print "\"%s\"," % word

print "]"


