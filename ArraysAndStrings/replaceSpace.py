'''
In python strings are immutable, so we will use a list to replace space with "%20" in in-place
First we calcualte the expected final length of the string after replacing the space
Here , we will use two pointers to perform in-place exchnange of characters
first pointer givenLength starts at the end char of original string
second pointer newstrLength at the end of the final string
we will continue until the first pointer reaches the start of the string
if we see " " we will replace  it with "%20" and decrease the second pointer by 3 and first pointer by 1 
else we will replace the char to the back and decrease first and second pointer by 1
'''
sentence = ["M","r"," ","J","o","h","n"," ","S","m","i","t","h"]
length = 13

def replaceSpace(sentence, length):
    givenLength = length -1
    newstrLength = 0
    for char in sentence:
        if char == " ":
            newstrLength += 3
        else:
            newstrLength += 1
    sentence += [' ']*(newstrLength - givenLength)

    while givenLength > 0:
        if sentence[givenLength] == " ":
            sentence[newstrLength] = "0"
            sentence[newstrLength - 1] = "2"
            sentence[newstrLength - 2] = "%"
            newstrLength -=3
            givenLength -= 1
        else:
            sentence[newstrLength] = sentence[givenLength]
            newstrLength -= 1
            givenLength -= 1
    
    return sentence

print(replaceSpace(sentence, length))
