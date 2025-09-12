# // Simple, given a string of words, return the length of the shortest word(s).

# // String will never be empty and you do not need to account for different data types.

def find_short(s):
    words = s.split()
    shortestLength= len(words[1])
    for word in words:
        if len(word) < shortestLength:
            shortestLength = len(word)
    return shortestLength