from sys import stdin

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def word_transformation_generator(w):
    """Return list of all valid step modifications for a given word"""
    # WARNING: This could be done much faster by using bytearray 
    # instead of inmutable strings but this is cleaner
    mods = []

    for pos in range(len(w)):
        # Del chars
        if len(w)>1:
            mods.append(w[:pos]+w[(pos+1):])  

        # Add chars
        for c in ALPHABET:      
            mods.append(w[:pos]+c+w[pos:])  
            
        # Mod chars
        for c in ALPHABET: 
            mods.append(w[:pos]+c+w[(pos+1):])  

    return mods



def find_longest_ladder(words):
    """ Words is in essence a DAG (Directed Acyclic Graph) in topological order
    So if we calculate the longest ladder from a word to the elements before it,
    the path won't change when we add more elements after it.
    Taking advantage of this fact  ...
    """
    # Initialize max length path for each word  
    wpath = {w: 0 for w in words[:-1]}

    # Longest step ladder found 
    longest_ladder_len = 0
    
    #
    for head in words:
        # Length for the longest ladder found for current word
        word_ladder_len = 0
       
        # Find longest ladder for each valid word transformation (if any)
        for w in word_transformation_generator(head):
            if w not in wpath:
                continue
            word_ladder_len = max(word_ladder_len, wpath[w]+1)

        wpath[head]=word_ladder_len
        longest_ladder_len = max(word_ladder_len, longest_ladder_len)

    return longest_ladder_len


if __name__ == '__main__':
    words=stdin.read().splitlines()
    print(find_longest_ladder(words))
