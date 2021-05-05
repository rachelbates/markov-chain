"""Generate Markov text from text files."""
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    #Opened the file and placed it into a contents variable as a string
    contents = open(file_path).read()

    return contents

chains_key_holder = []
chains = {}

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    split_words = text_string.split()

    #Create dictionary keys and empty list value
    #Create holder for tuples of keys (for easier reference for now)
    for i in range(len(split_words)-1): 
        chains[(split_words[i], split_words[i + 1])] = []
        chains_key_holder.append((split_words[i], split_words[i + 1]))
    
    #Loop though each word in split_words minus the last word
    #if the word appears in the key holder at the value before it, add the corresponding tuple to the dictionary and add on the word 
    for i in range(len(split_words) - 2) :
        if split_words[i+1] in chains_key_holder[i][1] :
            chains[chains_key_holder[i]] += [(split_words[i + 2])]

    return chains


def make_text(chains):
    """Return text from chains."""

    #Start with 2 words
    #Make a loop, end when you reach a word that has none after it.
    
    #Add first 2 key words' to "words" list
    #Begin loop until Key Value "I am?" is found empty
        #Find the new last two words' corresponding key in dictionary "chain"
        #Add this key's random value to "words" list

    words = []
    words += chains_key_holder[0]
    #Add the first key to the "words" list
    
    while True :
        if chains[(words[-2], words[-1])]:
            words.append(choice(chains[(words[-2], words[-1])]))
        else:
            break

    return ' '.join(words)



# Open the file and turn it into one long string
input_text = open_and_read_file("green-eggs.txt")

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
