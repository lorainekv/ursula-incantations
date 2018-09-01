import string
import random
import os

import tweepy
from dotenv import load_dotenv

from first_line.corpus import beluga_sevruga
from second_line.corpus import caspian_sea
from third_line.larynxes import larynxes 
from third_line.glossitis import glossitis 
from fourth_line.et import et
from fourth_line.laryngitis import laryngitis
from fifth_line.voices import voices

try:
    load_dotenv()
except: 
    pass

# Beluga, Sevruga
three_syllable_words = random.sample(beluga_sevruga, 2)
three_syllable_words = [string.capwords(word) for word in three_syllable_words]
line_one = ", ".join(three_syllable_words) + "\n"

# Come winds of the Caspian Sea
sea = random.choice(caspian_sea)
line_two = "Come winds of the %s\n" % sea

# Larynxes, glossitis
xes_ces = string.capwords(random.choice(larynxes))
itis = random.choice(glossitis)
line_three = "%s, %s\n" % (xes_ces, itis)

# Et max laryngitis
latin = random.choice(et)
other_itis = random.choice(laryngitis)
line_four = "%s %s \n" % (latin, other_itis)

# La voce to me
voice = random.choice(voices)
line_five = "%s to me" % voice

CONSUMER_KEY = os.environ.get("CONSUMER_KEY") 
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)

incantation = line_one + line_two + line_three + line_four + line_five
incantation = unicode(incantation, "utf-8")

api = tweepy.API(auth)
api.update_status(incantation)

