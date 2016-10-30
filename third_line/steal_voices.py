from textstat.textstat import textstat
from ces_xes import ces_xes

print("larynxes = [")
for word in ces_xes:
    syllables = round(textstat.syllable_count(word))
    if syllables == 3.0:
        print "\"%s\"," % word 

print "]" 

