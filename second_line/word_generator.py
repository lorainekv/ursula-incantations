import pronouncing as pr
import string

""" 
Substitutes for "Caspian" in "Caspian Sea":
    - Three syllables
    - Has the 100 syllable stress pattern
"""

def summon_seas():
    # Find words with mattching stress patterns
    caspian_phones = pr.phones_for_word("caspian")
    caspian_stresses = pr.stresses(caspian_phones[0])
    words_with_stress_pattern = pr.search_stresses(caspian_stresses)
    
    # Find words with correct syllable count
    three_syllable_words = []
    for word in words_with_stress_pattern:
        word_phones = pr.phones_for_word(word)
        syllable_count = pr.syllable_count(word_phones[0])
        if syllable_count == 3:
            sea = string.capwords((word + " sea"))
            three_syllable_words.append(sea)
    
    return three_syllable_words
