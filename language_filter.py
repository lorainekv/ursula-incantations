from profanity import profanity

def filter_words(word_list):
    '''
    Input an unfiltered list of words as the first arg

    Return a list of words not contained in the profanity banlist
    Arguments: 
        word_list: list of words
    Returns: filtered list of words 
    '''

    # Load custom offensive dictionary    
    filtered_words = []
    with open('offensive_filter.txt', 'r') as readfile:
        bad_words = readfile.readlines()
        bad_words = [word.strip() for word in bad_words]
        profanity.load_words(bad_words)
        
        for word in word_list:
            if not profanity.contains_profanity(word):
                print(word)
                filtered_words.append(word)

    return filtered_words 

