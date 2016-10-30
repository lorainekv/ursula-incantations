from textstat.textstat import textstat

from bodies_of_water import waters

print("caspian_sea = [")
for water in waters:
    syllables = round(textstat.syllable_count(water))
    if water.endswith("Sea") and syllables == 4.0:
        print "\"%s\"," % water

print "]"


