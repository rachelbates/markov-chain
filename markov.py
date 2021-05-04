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

    chains = {}

    split_words = text_string.split()
    
    #Loop through the words in split_words and assign as tuple in key
    chains_key_holder = []
    seuss_dictionary = {}

    for i in range(len(split_words) - 1):
        chains_key_holder.append((split_words[i], split_words[i + 1]))

    # DID NOT WORK
    # for future_key in range(len(chains_key_holder)-2):
    #     if chains_key_holder[i] in split_words:
    #         chains_key_holder[i]

        
   #THIS IS OUR OFFICIAL CURRENT ATTEMPT
    #loop through chains_key_holder.
    #for each future_key in chains_key_holder, check if future key is already a key in our dictionary. If not, assign future_key as a key the dictionary, 
    #then add (the following tuple's first index) as a value to future_key list.

    for i in range(len(chains_key_holder)-2): 
        
        #check if chains_key_holder[i] is a key yet
        #if not, create it as a key and add chains_key_holder[i+1][1] to the list of its values
        #if it IS already a key, add chains_key_holder[i+1][1] as its value
        #get() create chains_key_holder[i] as key
        #add chains_key_holder[i+1][1] as a value to a dictionary with chains_key_holder[i] as key




    print(chains_key_holder)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file("green-eggs.txt")

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
