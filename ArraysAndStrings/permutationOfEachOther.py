word1 = "test"
word2 ="tSet"

def permutationOfEachOther(word1, word2):
    for i in range(len(word1)):
        if word1[i] not in word2:
            return False

    return True

print(permutationOfEachOther(word1, word2))

#Method 2
#sort the two words
#compare each element/character if does not match return False
def isPermutated(word1, word2):
    word1 = sorted(word1.lower()) #if the case (upper or lower) does not matter
    word2 = sorted(word2.lower()) #if the case (upper or lower) does not matter
    if len(word1) != len(word2):
        return False

    for index in range(len(word1)):
        if word1[index] != word2[index]:
            return False
    return True

print(isPermutated(word1, word2))
