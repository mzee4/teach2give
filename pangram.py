# 3.Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Note: Pangrams are words or sentences containing every letter of the alphabet at least once. For example: "The quick brown fox jumps over the lazy dog"

def check_pangram(sentence):
    

    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in sentence:
            return "false"
    
    return "true"



sentence = "i went t safaricom today"
result = check_pangram(sentence)

if result == "true":
    print(f"{sentence} is a pangram")

else:
    print(f"{sentence} is not a pangram")