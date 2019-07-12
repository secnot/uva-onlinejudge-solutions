from sys import stdin
from string import ascii_lowercase

ALPHABET = ascii_lowercase


def word_transformations(w):
    """Return list of all valid step modifications for a given word"""
    # WARNING: This could be done much faster by using bytearray 
    # instead of inmutable strings but this is cleaner
    for pos in range(len(w)):
        # Delete the character
        if len(w)>1:
            yield w[:pos]+w[(pos+1):]

        # Add a character
        for c in ALPHABET:
            transform = w[:pos]+c+w[pos:]
            
            # break if it isn't in lexycographically order.
            if transform >= w:
                break
           
            yield transform

        # Mod chars
        for c in ALPHABET: 
            transform = w[:pos]+c+w[(pos+1):]
            
            # break if it isn't in lexycographically order.
            if transform >= w:
                break 
            
            yield transform

def find_longest_ladder(words):
    """ Words is in essence a DAG (Directed Acyclic Graph) in topological order
    So if we calculate the longest ladder starting with a word to the  elements 
    before it, the path won't change when we add more elements after it.
    Taking advantage of this fact we can incremetally calculate the longest path
    as new words are added.
    """
    # Initialize max length path for each word  
    wpath = {}
   
    # Iterate through input skipping the las new_line
    for w in words[:-1]:

        length = 1

        # Find longest ladder for each valid word transformation (if any)
        for transform in word_transformations(w):
         
            # If the transformation isn't lexycographically ordered ignore it
            if transform in wpath:
                length = max(length, wpath[transform]+1)
            
            wpath[w] = length

    # Find the longest constructed ladder
    return max(length for length in wpath.values())


if __name__ == '__main__':
    words=stdin.read().splitlines()
    print(find_longest_ladder(words))
