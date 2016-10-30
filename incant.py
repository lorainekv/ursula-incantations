import string
import random

from first_line.beluga_sevruga import beluga_sevruga 
from second_line.caspian_sea import caspian_sea
from third_line.larynxes import larynxes 
from third_line.glossitis import glossitis 
from fourth_line.et import et
from fourth_line.laryngitis import laryngitis
from fifth_line.voices import voices

# Beluga, Sevruga
three_syllable_words = random.sample(beluga_sevruga, 2)
three_syllable_words = [string.capwords(word) for word in three_syllable_words]
print ", ".join(three_syllable_words)

# Come winds of the Caspian Sea
sea = random.choice(caspian_sea)
print "Come winds of the %s" % sea

# Larynxes, glossitis
xes_ces = string.capwords(random.choice(larynxes))
itis = random.choice(glossitis)
print "%s, %s" % (xes_ces, itis)

# Et max laryngitis
latin = random.choice(et)
other_itis = random.choice(laryngitis)
print "%s, %s" % (latin, other_itis)

# La voce to me
voice = string.capwords(random.choice(voices))
print "%s to me" % voice
