
# ! Initializing Variables
# We start by initializing an empty unordered map called mp (short for map), which will store the groups of anagrams.
# Grouping Anagrams
# We iterate through each word in the input vector strs. Let's take the first word, "eat", as an example.

# ! Sorting the Word
# We create a string variable called word and assign it the value of the current word ("eat" in this case).
# Next, we sort the characters in word using the sort() function. After sorting, word becomes "aet".

# ! Grouping the Anagram
# We insert word as the key into the mp unordered map using mp[word], and we push the original word ("eat") into the vector associated with that key using mp[word].append(x), where x is the current word.
# Since "aet" is a unique sorted representation of all the anagrams, it serves as the key in the mp map, and the associated vector holds all the anagrams.
# Creating the Result
# We initialize an empty vector called ans (short for answer) to store the final result.

# We iterate through each key-value pair in the mp map using a for loop. For each pair, we append the vector of anagrams (x[1]) into the ans vector.


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())