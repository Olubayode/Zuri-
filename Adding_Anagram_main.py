# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word_ = list(word)
    word_.sort()
    anagram_ = list(anagram)
    anagram_.sort()

    return (word_ == anagram_)

word= "car"
anagram = "arc"
word2 = 'Zuri'
anagram2 = 'Uric'

find_anagram(word, anagram)
find_anagram(word2, anagram2)