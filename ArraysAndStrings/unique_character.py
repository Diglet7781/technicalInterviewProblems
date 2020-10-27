inputString = "abcde"

#Brute Force Approach with runtime complexity of O(n2)
def uniqueBruteForceCharacter(inputString):
    if len(inputString) == 1:
        return True
    for index in range(len(inputString)):
        for nextIndex in range(index + 1, len(inputString)):
            if inputString[index] == inputString[nextIndex]:
                return False
    
    return True

#HashMap approach with runtime complixity of O(n), space complexity of O(n)
def uniqueCharacterHashMap(inputString):
    if len(inputString) == 1:
        return True
    seen = dict()
    for index in range(len(inputString)):
        if inputString[index] not in seen:
            seen[inputString[index]] = index
        else:
            return False
    return True

print(uniqueBruteForceCharacter(inputString))
print(uniqueCharacterHashMap(inputString))