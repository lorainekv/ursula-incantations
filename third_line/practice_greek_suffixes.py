from textstat.textstat import textstat
from itis import itis 

print("glossitis = [")
for word in itis:
    syllables = round(textstat.syllable_count(word))
    if syllables == 3.0:
        print "\"%s\"," % word 

print "]" 
