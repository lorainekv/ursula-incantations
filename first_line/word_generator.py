import pronouncing as pr

""" 
Substitutes for "Beluga, sevruga":
    - Three syllables
    - Has a ˘`˘ syllable stress pattern
    - Ends with AH0 (ARPAbet phonetic notation)
"""

def find_words():
    # Find words with mattching stress patterns
    beluga_phones = pr.phones_for_word("beluga")
    last_beluga_phone = pr.phones_for_word("beluga")[0].split(" ")[-1]
    beluga_stresses = pr.stresses(beluga_phones[0])
    words_with_stress_pattern = pr.search_stresses(beluga_stresses)
    
    # Find words with matching end phone
    words_ending_with_ah = pr.search(last_beluga_phone + "$")
    
    
    # Find words with correct syllable count
    words_with_stress_and_ending = list(set(words_with_stress_pattern).intersection(words_ending_with_ah))
    three_syllable_words = []
    for word in words_with_stress_and_ending:
        word_phones = pr.phones_for_word(word)
        syllable_count = pr.syllable_count(word_phones[0])
        if syllable_count == 3:
            three_syllable_words.append(word)
    
    return three_syllable_words

