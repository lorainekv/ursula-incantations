from textstat.textstat import textstat
from itis import itis 

print("laryngitis = [")
for word in itis:
    syllables = round(textstat.syllable_count(word))
    if syllables == 4.0:
        print "\"%s\"," % word 

print "]" 

