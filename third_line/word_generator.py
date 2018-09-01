import pronouncing as pr
import string

""" 
Substitutes for "Larynxes":
    - Three syllables
    - Ends with "S IH0 Z" or "S IH0 S" sound (ARPAbet notation), such as "morasses" or "Alexis"
    - Has a ``˘ syllable stress pattern
"""

def steal_voices():
    words_ending_with_sounds = pr.search("S IH0 [ZS]$") 
    words_with_stresses = pr.search_stresses('[12][12]0')
    words_with_sounds_and_stresses = set(words_ending_with_sounds).intersection(words_with_stresses) 
    
    # Find words with correct syllable count
    three_syllable_words = []
    for word in words_with_sounds_and_stresses:
        word_phones = pr.phones_for_word(word)
        syllable_count = pr.syllable_count(word_phones[0])
        if syllable_count == 3:
            three_syllable_words.append(word)
    
    return three_syllable_words
