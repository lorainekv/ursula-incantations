import random
from first_line.beluga_sevruga import beluga_sevruga 
from second_line.caspian_sea import caspian_sea
from third_line.larynxes import larynxes 
from third_line.itis import itis 

# Beluga, Sevruga
three_syllable_words = random.sample(beluga_sevruga, 2)
three_syllable_words = [word.title() for word in three_syllable_words]
print ", ".join(three_syllable_words)

# Come winds of the Caspian Sea
sea = random.choice(caspian_sea)
print "Come winds of the %s" % sea

# Larynxes, glossitis
xes_ces = random.choice(larynxes).title()
itis = random.choice(itis)
print "%s, %s" % (xes_ces, itis)

