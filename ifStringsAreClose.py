'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

'''

def closeStrings(self, word1: str, word2: str) -> bool:
	if set(word1) != set(word2):
            return False
        a = sorted(list(Counter(word1).values()))
        b = sorted(list(Counter(word2).values()))
        if a != b:
            return False
        else:
            return True
